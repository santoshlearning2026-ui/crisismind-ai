"""Recommendation agent."""

import logging
from typing import Dict, Any

from app.agents.base import BaseAgent
from app.services.gemini_service import gemini_service

logger = logging.getLogger(__name__)


class RecommendationAgent(BaseAgent):
    """Recommendation generation agent."""

    def __init__(self):
        """Initialize recommendation agent."""
        super().__init__(
            name="RecommendationAgent",
            description="Generates actionable recommendations",
        )

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute recommendation agent.
        
        Args:
            input_data: Input data with risk level and context
            
        Returns:
            Recommendations
        """
        city = input_data.get("city")
        risk_level = input_data.get("risk_level", "moderate")
        logger.info(f"Recommendation agent processing: {city}")
        
        recommendations = await gemini_service.generate_recommendations(city, risk_level)
        
        return {
            "agent": self.name,
            "status": "success",
            "data": {"recommendations": recommendations},
        }


recommendation_agent = RecommendationAgent()
