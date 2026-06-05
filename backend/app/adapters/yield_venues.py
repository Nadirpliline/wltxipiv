"""Yield venue adapter (Aave v3, Morpho, tokenized T-bills).

Surfaces current APYs and supports deposit/withdraw of idle treasury under the
organization's policy. Sandbox APYs are indicative and deterministic.
"""

from __future__ import annotations

from app.adapters.base import Adapter

# venue -> (asset, chain, apy, risk_tier)
_VENUES = {
    "aave_v3_usdc": ("USDC", "base", 0.0512, "low"),
    "morpho_usdc": ("USDC", "base", 0.0648, "low-mid"),
    "ondo_ousg": ("USDC", "ethereum", 0.0489, "t-bill"),
    "aave_v3_usdt": ("USDT", "arbitrum", 0.0473, "low"),
}


class YieldAdapter(Adapter):
    name = "yield"

    def list_venues(self, asset: str | None = None) -> list[dict]:
        out = []
        for venue, (vasset, chain, apy, risk) in _VENUES.items():
            if asset and vasset != asset.upper():
                continue
            out.append(
                {"venue": venue, "asset": vasset, "chain": chain, "apy": apy, "risk_tier": risk}
            )
        return sorted(out, key=lambda v: v["apy"], reverse=True)

    def best_venue(self, asset: str = "USDC") -> dict | None:
        venues = self.list_venues(asset)
        return venues[0] if venues else None

    def project_annual_income(self, principal_usd: float, apy: float) -> float:
        return round(principal_usd * apy, 2)


yield_adapter = YieldAdapter()
