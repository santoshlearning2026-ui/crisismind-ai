"""News agent."""

import logging
from typing import Dict, Any

from app.agents.base import BaseAgent
from app.services.news_service import news_service

logger = logging.getLogger(__name__)


class NewsAgent(BaseAgent):
    """News and event monitoring agent."""

    def __init__(self):
        """Initialize news agent."""
        super().__init__(
            name="NewsAgent",
            description="Monitors relevant news and events",
        )

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute news agent.
        
        Args:
            input_data: Input data with city name
            
        Returns:
            News data
        """
        city = input_data.get("city")
        logger.info(f"News agent processing: {city}")
        
        news_data = await news_service.get_recent_news(city)
        
        return {
            "agent": self.name,
            "status": "success",
            "data": {"articles": news_data},
        }


news_agent = NewsAgent()
