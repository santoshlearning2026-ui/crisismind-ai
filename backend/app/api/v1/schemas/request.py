"""Request schemas."""

from typing import Optional

from pydantic import BaseModel, Field


class RiskPredictionRequest(BaseModel):
    """Risk prediction request."""

    city: str = Field(..., min_length=1, max_length=100, description="City name")
    risk_types: Optional[list] = Field(
        default=None, description="Specific risk types to predict"
    )


class SimulationRequest(BaseModel):
    """Simulation request."""

    city: str = Field(..., description="City name")
    scenario: str = Field(..., description="Scenario description")
    parameters: Optional[dict] = Field(default=None, description="Simulation parameters")


class WeatherQueryRequest(BaseModel):
    """Weather query request."""

    city: str = Field(..., description="City name")
    include_forecast: bool = Field(default=False, description="Include forecast data")


class ExplanationRequest(BaseModel):
    """Explanation request."""

    city: str = Field(..., description="City name")
    risk_type: str = Field(..., description="Risk type for explanation")
    detail_level: str = Field(
        default="summary", description="Detail level: summary, detailed, technical"
    )
