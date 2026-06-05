"""Settlement routing: pick the cheapest viable chain for a payout.

The agent uses this to auto-select the lowest-cost network a payee can receive
on, honouring the payee's preferred chain when set.
"""

from __future__ import annotations

from app.core.constants import CHAIN_TX_COST_USD, Chain


def cheapest_chain(candidates: list[str] | None = None) -> str:
    pool = candidates or [c.value for c in Chain]
    return min(pool, key=lambda c: CHAIN_TX_COST_USD.get(Chain(c), 99.0))


def tx_cost_usd(chain: str) -> float:
    return CHAIN_TX_COST_USD.get(Chain(chain), 1.0)


def select_route(
    *, preferred_chain: str | None, auto_select_cheapest: bool, payee_address: str
) -> tuple[str, float]:
    """Return ``(chain, fee_usd)`` for a payout.

    Solana addresses (base58, no 0x) cannot receive on EVM and vice-versa, so the
    candidate pool is constrained by the payee's address format.
    """
    is_evm = payee_address.startswith("0x")
    evm = [Chain.BASE, Chain.POLYGON, Chain.ARBITRUM, Chain.OPTIMISM, Chain.ETHEREUM]
    pool = [c.value for c in evm] if is_evm else [Chain.SOLANA.value]

    if preferred_chain in pool and not auto_select_cheapest:
        chain = preferred_chain
    else:
        chain = cheapest_chain(pool)
    return chain, tx_cost_usd(chain)
