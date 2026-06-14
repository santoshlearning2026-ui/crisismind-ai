"""Explanation endpoints."""

from datetime import datetime

from fastapi import APIRouter

from app.api.v1.schemas.response import ExplanationResponse

router = APIRouter()


@router.get("/explanations/{city}", response_model=ExplanationResponse)
async def get_risk_explanation(city: str, risk_type: str = "flood") -> ExplanationResponse:
    """Get explanation for risk assessment.
    
    Args:
        city: City name
        risk_type: Risk type
        
    Returns:
        Explanation response
    """
    # Placeholder implementation
    return ExplanationResponse(
        city=city,
        risk_type=risk_type,
        explanation=f"The {risk_type} risk in {city} is elevated due to recent weather patterns and infrastructure conditions.",
        factors=[
            {"factor": "Recent rainfall", "impact": "high", "weight": 0.3},
            {"factor": "River proximity", "impact": "high", "weight": 0.25},
            {"factor": "Drainage infrastructure", "impact": "medium", "weight": 0.2},
        ],
        recommendations=[
            "Increase emergency preparedness",
            "Monitor weather conditions",
            "Activate warning systems",
        ],
        timestamp=datetime.utcnow(),
    )
