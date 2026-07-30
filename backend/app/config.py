# Read Web Configuration
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = (
    Path(__file__).resolve().parents[2]
)  # simple-web-app/ (root parent project)
ENV_FILE = PROJECT_ROOT / ".env"


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Values are injected from environment/.env at runtime by pydantic-settings.
settings = Settings()  # type: ignore[call-arg]
