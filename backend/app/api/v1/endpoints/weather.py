"""Weather endpoints."""

from datetime import datetime

from fastapi import APIRouter

from app.api.v1.schemas.response import WeatherDataResponse

router = APIRouter()


@router.get("/weather/{city}", response_model=WeatherDataResponse)
async def get_weather_data(city: str) -> WeatherDataResponse:
    """Get weather data for a city.
    
    Args:
        city: City name
        
    Returns:
        Weather data response
    """
    # Placeholder implementation
    return WeatherDataResponse(
        city=city,
        temperature=28.5,
        humidity=65.0,
        precipitation=0.0,
        wind_speed=12.3,
        pressure=1013.25,
        timestamp=datetime.utcnow(),
    )
