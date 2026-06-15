"""Prediction agent."""

import logging
from typing import Dict, Any

from app.agents.base import BaseAgent
from app.services.risk_service import risk_service

logger = logging.getLogger(__name__)


class PredictionAgent(BaseAgent):
    """Risk prediction agent."""

    def __init__(self):
        """Initialize prediction agent."""
        super().__init__(
            name="PredictionAgent",
            description="Generates risk predictions using ML models",
        )

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute prediction agent.
        
        Args:
            input_data: Input data with features
            
        Returns:
            Risk predictions
        """
        city = input_data.get("city")
        features = input_data.get("features", {})
        logger.info(f"Prediction agent processing: {city}")
        
        predictions = await risk_service.get_all_risks(city, features)
        
        return {
            "agent": self.name,
            "status": "success",
            "data": predictions,
        }


prediction_agent = PredictionAgent()
