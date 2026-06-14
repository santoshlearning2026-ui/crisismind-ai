"""Validation utilities."""

from typing import Any


def validate_city_name(city: str) -> bool:
    """Validate city name format.
    
    Args:
        city: City name to validate
        
    Returns:
        True if valid, False otherwise
    """
    return len(city) > 0 and len(city) <= 100 and city.isalpha()


def validate_risk_score(score: float) -> bool:
    """Validate risk score is between 0 and 100.
    
    Args:
        score: Risk score
        
    Returns:
        True if valid, False otherwise
    """
    return 0 <= score <= 100


def validate_coordinates(lat: float, lon: float) -> bool:
    """Validate geographic coordinates.
    
    Args:
        lat: Latitude
        lon: Longitude
        
    Returns:
        True if valid, False otherwise
    """
    return -90 <= lat <= 90 and -180 <= lon <= 180
