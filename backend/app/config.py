"""Application Configuration."""

from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # Application
    APP_NAME: str = "CRISISMIND AI"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    DEBUG: bool = False
    SECRET_KEY: str = "your-secret-key-change-in-production"

    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/crisismind_db"
    DATABASE_ECHO: bool = False
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10

    # Redis (optional)
    REDIS_URL: str = "redis://localhost:6379/0"

    # API Keys
    GEMINI_API_KEY: str = ""
    OPENWEATHER_API_KEY: str = ""
    NEWS_API_KEY: str = ""

    # ChromaDB
    CHROMADB_HOST: str = "localhost"
    CHROMADB_PORT: int = 8000
    CHROMADB_COLLECTION: str = "crisismind_vectors"

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    CORS_ALLOW_CREDENTIALS: bool = True

    # Security
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    TRUST_PROXY: bool = False

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    # Features
    FEATURE_WEBSOCKET: bool = False
    FEATURE_GRAPHQL: bool = False
    FEATURE_CACHING: bool = True

    # Model Configuration
    MODEL_VERSION: str = "1.0"
    MODEL_CACHE_SIZE: int = 1000

    # Agent Configuration
    AGENT_TIMEOUT: int = 30
    AGENT_MAX_RETRIES: int = 3
    AGENT_BATCH_SIZE: int = 100

    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 60

    # Cache
    CACHE_TTL: int = 3600
    CACHE_MAX_SIZE: int = 10000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
