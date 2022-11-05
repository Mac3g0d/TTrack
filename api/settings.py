import uuid
from functools import lru_cache

from pydantic import BaseSettings, Field, RedisDsn, SecretStr, validator


class Settings(BaseSettings):
    """Project settings."""

    SESSION_SECRET_KEY: str = Field(default=str(uuid.uuid4()))

    CORS_ORIGINS: str = "*"
    CORS_METHODS: list[str] = ["GET", "POST", "OPTIONS"]
    CORS_HEADERS: list[str] = ["*"]

    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

    DATABASE_URI: str | None

    KEYDB_URL: RedisDsn
    KEYDB_PASSWORD: str

    @validator("DATABASE_URI", pre=True)
    @classmethod
    def validate_postgres_uri(cls, v: str | None, values: dict[str, str | None]) -> str:  # noqa: N805, WPS111, VNE001, ANN102, E501, WPS210
        """
        Generate a database url.

        :param v: database url parameter (default=None)
        :param values: values of settings inited before this parameter
        :return: str.
        """
        if isinstance(v, str):
            return v
        user: str = values.get("POSTGRES_USER")
        password: SecretStr = values.get("POSTGRES_PASSWORD", SecretStr("")).get_secret_value()
        host: str = values.get("POSTGRES_HOST")
        port: str = values.get("POSTGRES_PORT")
        db: str = values.get("POSTGRES_DB")
        database_url = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"  # noqa: WPS221
        return database_url  # noqa: WPS331

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance.

    :return: Settings instance.
    """
    return Settings()
