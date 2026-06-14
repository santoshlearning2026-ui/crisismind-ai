"""Formatting utilities."""

from datetime import datetime
from typing import Dict, Any


def format_risk_level(score: float) -> str:
    """Format risk score to risk level.
    
    Args:
        score: Risk score (0-100)
        
    Returns:
        Risk level string
    """
    if score < 25:
        return "low"
    elif score < 50:
        return "moderate"
    elif score < 75:
        return "high"
    else:
        return "critical"


def format_timestamp(dt: datetime) -> str:
    """Format datetime to ISO string.
    
    Args:
        dt: Datetime object
        
    Returns:
        ISO formatted string
    """
    return dt.isoformat()


def format_response(
    status: str,
    data: Any = None,
    message: str = "",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Format API response.
    
    Args:
        status: Response status
        data: Response data
        message: Response message
        **kwargs: Additional fields
        
    Returns:
        Formatted response dictionary
    """
    response: Dict[str, Any] = {
        "status": status,
        "timestamp": datetime.utcnow().isoformat(),
    }

    if message:
        response["message"] = message

    if data is not None:
        response["data"] = data

    response.update(kwargs)
    return response
