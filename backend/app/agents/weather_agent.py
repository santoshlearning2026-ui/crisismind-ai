"""Weather agent."""

import logging
from typing import Dict, Any

from app.agents.base import BaseAgent
from app.services.weather_service import weather_service

logger = logging.getLogger(__name__)


class WeatherAgent(BaseAgent):
    """Weather data collection agent."""

    def __init__(self):
        """Initialize weather agent."""
        super().__init__(
            name="WeatherAgent",
            description="Collects and processes weather data",
        )

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute weather agent.
        
        Args:
            input_data: Input data with city name
            
        Returns:
            Weather data
        """
        city = input_data.get("city")
        logger.info(f"Weather agent processing: {city}")
        
        weather_data = await weather_service.get_current_weather(city)
        
        return {
            "agent": self.name,
            "status": "success",
            "data": weather_data,
        }


weather_agent = WeatherAgent()
