"""Idempotent demo seed.

Creates a realistic crypto-native org ("Helios Labs DAO") with multi-chain
multisig wallets, balances, a yield position, an opening capital + revenue
ledger, contractors, and a few uncategorized transactions so every screen and
the agent have meaningful data on first run.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.constants import TxStatus, TxType
from app.models import (
    Contractor,
    Organization,
    Transaction,
    TreasuryPolicy,
    Wallet,
    YieldPosition,
)
from app.models.treasury import WalletBalance
from app.services import ledger_service

DEMO_SLUG = "helios-labs"


def _balance(wallet: Wallet, asset: str, amount: float, price: float = 1.0) -> WalletBalance:
    return WalletBalance(wallet=wallet, asset=asset, amount=amount, usd_price=price)


def seed_demo(db: Session, *, force: bool = False) -> Organization:
    existing = db.scalar(select(Organization).where(Organization.slug == DEMO_SLUG))
    if existing and not force:
        return existing
    if existing and force:
        db.delete(existing)
        db.flush()

    org = Organization(
        name="Helios Labs DAO",
        slug=DEMO_SLUG,
        legal_entity="Helios Labs Foundation (Cayman)",
        base_currency="USD",
        base_stablecoin="USDC",
    )
    db.add(org)
    db.flush()

    db.add(
        TreasuryPolicy(
            organization_id=org.id,
            min_operating_reserve_usd=250_000.0,
            target_stablecoin_pct=0.85,
            idle_yield_threshold_usd=100_000.0,
            target_yield_apy=0.05,
            max_autonomous_transfer_usd=25_000.0,
            max_autonomous_daily_usd=150_000.0,
            required_signatures=2,
            preferred_chain="base",
            auto_select_cheapest_chain=True,
        )
    )

    # Multisig wallets across chains.
    safe_base = Wallet(
        organization_id=org.id, label="Ops Safe (Base)", chain="base",
        address="0x5aFE000000000000000000000000000000Ba53", kind="safe", threshold=2, owners=4,
    )
    safe_eth = Wallet(
        organization_id=org.id, label="Treasury Safe (Ethereum)", chain="ethereum",
        address="0x5aFE000000000000000000000000000000E711", kind="safe", threshold=3, owners=5,
    )
    safe_arb = Wallet(
        organization_id=org.id, label="Ops Safe (Arbitrum)", chain="arbitrum",
        address="0x5aFE000000000000000000000000000000A912", kind="safe", threshold=2, owners=4,
    )
    squads_sol = Wallet(
        organization_id=org.id, label="Grants Squads (Solana)", chain="solana",
        address="So1Mu1t1s1gSquadsVau1tPDA00000000000000000", kind="squads", threshold=2, owners=3,
    )
    db.add_all([safe_base, safe_eth, safe_arb, squads_sol])
    db.flush()

    db.add_all(
        [
            _balance(safe_base, "USDC", 1_240_000),
            _balance(safe_base, "USDT", 180_000),
            _balance(safe_eth, "USDC", 600_000),
            _balance(safe_eth, "ETH", 140, 3150.0),
            _balance(safe_eth, "WBTC", 3.5, 64200.0),
            _balance(safe_arb, "USDC", 320_000),
            _balance(squads_sol, "USDC", 210_000),
            _balance(squads_sol, "SOL", 1_800, 152.0),
        ]
    )

    db.add(
        YieldPosition(
            organization_id=org.id, venue="morpho_usdc", chain="base", asset="USDC",
            principal_usd=750_000, apy=0.0648, accrued_yield_usd=12_480,
        )
    )

    # Chart of accounts + opening ledger.
    ledger_service.ensure_chart_of_accounts(db, org.id)
    ledger_service.post_entry(
        db, organization_id=org.id,
        lines=[("1000", 2_000_000, 0.0), ("3000", 0.0, 2_000_000)],
        memo="Opening capital contribution (seed round)", reference="opening", source="manual",
    )
    ledger_service.post_entry(
        db, organization_id=org.id,
        lines=[("1000", 480_000, 0.0), ("4000", 0.0, 480_000)],
        memo="Protocol revenue — Q2 fees", reference="rev-q2", source="agent",
    )
    ledger_service.post_entry(
        db, organization_id=org.id,
        lines=[("1100", 750_000, 0.0), ("1000", 0.0, 750_000)],
        memo="Deploy idle USDC to Morpho", reference="yield:morpho_usdc", source="agent",
    )
    ledger_service.post_entry(
        db, organization_id=org.id,
        lines=[("1100", 12_480, 0.0), ("4100", 0.0, 12_480)],
        memo="Accrued yield income (Morpho)", reference="yield-accrual", source="agent",
    )

    # Contractors directory.
    db.add_all(
        [
            Contractor(organization_id=org.id, name="Aisha Bello", email="aisha@helios.xyz",
                       country="NG", role="Smart Contract Engineer", payout_chain="base",
                       wallet_address="0xA15ha000000000000000000000000000000be110",
                       kyc_status="cleared"),
            Contractor(organization_id=org.id, name="Diego Santos", email="diego@helios.xyz",
                       country="BR", role="DevRel", payout_chain="solana",
                       wallet_address="DiegoSo1anaWa11et000000000000000000000000", kyc_status="cleared"),
            Contractor(organization_id=org.id, name="Mei Tanaka", email="mei@helios.xyz",
                       country="JP", role="Designer", payout_chain="base",
                       wallet_address="0xMe1000000000000000000000000000000Tanaka1", kyc_status="cleared"),
        ]
    )

    # A few uncategorized transactions for the agent to reconcile.
    db.add_all(
        [
            Transaction(organization_id=org.id, tx_type=TxType.VENDOR, status=TxStatus.EXECUTED,
                        chain="base", asset="USDC", amount=4_200, usd_value=4_200,
                        counterparty="Vercel Inc", to_address="0xVerce1", memo="Frontend hosting",
                        category="uncategorized", tx_hash="0xseed01", created_by="agent"),
            Transaction(organization_id=org.id, tx_type=TxType.VENDOR, status=TxStatus.EXECUTED,
                        chain="base", asset="USDC", amount=18_000, usd_value=18_000,
                        counterparty="Deloitte LLP", to_address="0xDe1o1tte", memo="Annual audit retainer",
                        category="uncategorized", tx_hash="0xseed02", created_by="agent"),
            Transaction(organization_id=org.id, tx_type=TxType.SWAP, status=TxStatus.EXECUTED,
                        chain="base", asset="USDC", amount=100_000, usd_value=100_000,
                        counterparty="Li.Fi", memo="Swap USDT->USDC rebalance",
                        category="uncategorized", tx_hash="0xseed03", created_by="agent"),
        ]
    )

    db.flush()
    db.commit()
    return org
