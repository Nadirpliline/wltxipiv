"""Application configuration.

Settings are read from environment variables (and an optional .env file) so the
service runs out of the box with SQLite while remaining production-ready for
Postgres. No secrets are required for the deterministic agent to operate; if an
LLM key is supplied the agent core upgrades to model-driven planning.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="MANDATE_", env_file=".env", extra="ignore")

    # Core
    app_name: str = "Mandate"
    environment: str = "local"
    api_v1_prefix: str = "/api/v1"

    # Persistence. SQLite by default; set MANDATE_DATABASE_URL to a Postgres DSN
    # (e.g. postgresql+psycopg://user:pass@host/db) for production.
    database_url: str = "sqlite:///./data/mandate.db"

    # Agent / LLM. When empty, the deterministic policy engine drives the agent.
    llm_provider: str = "deterministic"  # one of: deterministic | anthropic | openai
    anthropic_api_key: str = ""
    openai_api_key: str = ""
    llm_model: str = "claude-sonnet-4"

    # Treasury policy defaults (organization-level overrides live in the DB).
    base_stablecoin: str = "USDC"
    min_operating_reserve_usd: float = 50_000.0
    idle_yield_threshold_usd: float = 100_000.0
    max_agent_autonomous_transfer_usd: float = 25_000.0

    # External integrations (live mode requires keys; sandbox is the default).
    integration_mode: str = "sandbox"  # sandbox | live
    bridge_api_base: str = "https://api.bridge.xyz"
    bridge_api_key: str = ""
    lifi_api_base: str = "https://li.quest/v1"

    # CORS
    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
