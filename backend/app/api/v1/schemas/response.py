"""Response schemas."""

from datetime import datetime
from typing import Optional, Dict, Any, List

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response."""

    status: str = Field(..., description="Health status")
    timestamp: datetime = Field(..., description="Check timestamp")
    version: str = Field(..., description="API version")
    checks: Dict[str, str] = Field(default_factory=dict, description="Component checks")


class RiskScoreResponse(BaseModel):
    """Risk score response."""

    city: str = Field(..., description="City name")
    risk_type: str = Field(..., description="Risk type")
    score: float = Field(..., ge=0, le=100, description="Risk score 0-100")
    level: str = Field(..., description="Risk level")
    confidence: float = Field(..., ge=0, le=1, description="Prediction confidence")
    timestamp: datetime = Field(..., description="Prediction timestamp")


class RiskPredictionResponse(BaseModel):
    """Risk prediction response."""

    city: str = Field(..., description="City name")
    predictions: List[RiskScoreResponse] = Field(
        ..., description="Risk predictions"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )


class WeatherDataResponse(BaseModel):
    """Weather data response."""

    city: str = Field(..., description="City name")
    temperature: float = Field(..., description="Temperature in Celsius")
    humidity: float = Field(..., description="Humidity percentage")
    precipitation: float = Field(..., description="Precipitation in mm")
    wind_speed: float = Field(..., description="Wind speed in km/h")
    pressure: float = Field(..., description="Atmospheric pressure")
    timestamp: datetime = Field(..., description="Data timestamp")


class SimulationResultResponse(BaseModel):
    """Simulation result response."""

    simulation_id: str = Field(..., description="Simulation ID")
    city: str = Field(..., description="City name")
    scenario: str = Field(..., description="Scenario name")
    results: Dict[str, Any] = Field(..., description="Simulation results")
    timestamp: datetime = Field(..., description="Simulation timestamp")


class ExplanationResponse(BaseModel):
    """Explanation response."""

    city: str = Field(..., description="City name")
    risk_type: str = Field(..., description="Risk type")
    explanation: str = Field(..., description="Risk explanation")
    factors: List[Dict[str, Any]] = Field(..., description="Contributing factors")
    recommendations: List[str] = Field(..., description="Recommendations")
    timestamp: datetime = Field(..., description="Explanation timestamp")


class ErrorResponse(BaseModel):
    """Error response."""

    status: str = Field(default="error", description="Status")
    code: str = Field(..., description="Error code")
    message: str = Field(..., description="Error message")
    details: Optional[Dict[str, Any]] = Field(default=None, description="Error details")
