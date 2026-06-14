"""Application Constants."""

from enum import Enum


class RiskLevel(str, Enum):
    """Risk levels."""

    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


class RiskType(str, Enum):
    """Risk types."""

    FLOOD = "flood"
    HEATWAVE = "heatwave"
    POWER_OUTAGE = "power_outage"


class AgentType(str, Enum):
    """Agent types."""

    WEATHER = "weather"
    INFRASTRUCTURE = "infrastructure"
    NEWS = "news"
    PREDICTION = "prediction"
    RECOMMENDATION = "recommendation"
    ORCHESTRATOR = "orchestrator"


class DataSource(str, Enum):
    """Data sources."""

    WEATHER_API = "weather_api"
    NEWS_API = "news_api"
    GEMINI = "gemini"
    USER_UPLOAD = "user_upload"


# Risk thresholds (0-100)
RISK_THRESHOLDS = {
    "LOW": (0, 25),
    "MODERATE": (25, 50),
    "HIGH": (50, 75),
    "CRITICAL": (75, 100),
}

# API response limits
DEFAULT_PAGE_SIZE = 50
MAX_PAGE_SIZE = 500
DEFAULT_TIMEOUT = 30

# Cache durations (seconds)
CACHE_HEALTH_CHECK = 60
CACHE_RISK_DATA = 3600
CACHE_WEATHER_DATA = 1800
