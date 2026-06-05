"""Multi-chain treasury adapters: Safe (EVM) and Squads (Solana).

The agent never holds private keys. For EVM it builds a Safe transaction and
returns a ``safe_tx_hash`` that owners co-sign; for Solana it builds a Squads
proposal. In sandbox mode these produce deterministic, well-formed identifiers
so the multisig lifecycle (propose → collect signatures → execute) can be driven
end-to-end. In live mode the same methods would call the Safe Transaction
Service / Squads program via viem / @solana/web3.js equivalents.
"""

from __future__ import annotations

import hashlib

from app.adapters.base import Adapter
from app.core.constants import EVM_CHAINS, Chain


def _det_hash(prefix: str, *parts: object) -> str:
    raw = "|".join(str(p) for p in parts)
    digest = hashlib.sha256(raw.encode()).hexdigest()
    return f"{prefix}{digest[:64]}"


class SafeAdapter(Adapter):
    """EVM multisig (Safe / Gnosis Safe) co-signer adapter."""

    name = "safe"

    def build_transfer(
        self, *, chain: str, safe_address: str, to: str, asset: str, amount: float, nonce: int
    ) -> dict:
        safe_tx_hash = _det_hash("0x", "safe", chain, safe_address, to, asset, amount, nonce)
        return {
            "type": "safe_multisig_tx",
            "chain": chain,
            "safe_address": safe_address,
            "to": to,
            "asset": asset,
            "amount": amount,
            "nonce": nonce,
            "safe_tx_hash": safe_tx_hash,
            "service_url": f"https://safe-transaction-{chain}.safe.global",
        }

    def execute(self, *, safe_tx_hash: str) -> dict:
        return {
            "executed": True,
            "tx_hash": _det_hash("0x", "exec", safe_tx_hash),
            "safe_tx_hash": safe_tx_hash,
        }


class SquadsAdapter(Adapter):
    """Solana multisig (Squads v4) co-signer adapter."""

    name = "squads"

    def build_transfer(
        self, *, multisig: str, to: str, asset: str, amount: float, index: int
    ) -> dict:
        proposal = hashlib.sha256(
            f"squads|{multisig}|{to}|{asset}|{amount}|{index}".encode()
        ).hexdigest()
        return {
            "type": "squads_proposal",
            "chain": Chain.SOLANA,
            "multisig": multisig,
            "to": to,
            "asset": asset,
            "amount": amount,
            "transaction_index": index,
            "proposal_pda": proposal[:44],
            "safe_tx_hash": proposal[:44],
        }

    def execute(self, *, safe_tx_hash: str) -> dict:
        sig = hashlib.sha256(f"squads-exec|{safe_tx_hash}".encode()).hexdigest()
        return {"executed": True, "tx_hash": sig[:88], "safe_tx_hash": safe_tx_hash}


_safe = SafeAdapter()
_squads = SquadsAdapter()


def get_chain_adapter(chain: str):
    """Return the correct multisig adapter for a chain."""
    if chain == Chain.SOLANA:
        return _squads
    if chain in EVM_CHAINS:
        return _safe
    raise ValueError(f"Unsupported chain: {chain}")
