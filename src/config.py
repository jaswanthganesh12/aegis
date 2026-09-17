from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Aegis"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    API_PREFIX: str = "/api/v1"

    REDIS_URL: str = "redis://localhost:6379"

    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:password@localhost:5432/aegis_db"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()