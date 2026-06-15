"""Infrastructure agent."""

import logging
from typing import Dict, Any

from app.agents.base import BaseAgent
from app.services.infrastructure_service import infrastructure_service

logger = logging.getLogger(__name__)


class InfrastructureAgent(BaseAgent):
    """Infrastructure assessment agent."""

    def __init__(self):
        """Initialize infrastructure agent."""
        super().__init__(
            name="InfrastructureAgent",
            description="Analyzes infrastructure vulnerability",
        )

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute infrastructure agent.
        
        Args:
            input_data: Input data with city name
            
        Returns:
            Infrastructure assessment
        """
        city = input_data.get("city")
        logger.info(f"Infrastructure agent processing: {city}")
        
        infra_data = await infrastructure_service.get_city_infrastructure(city)
        
        return {
            "agent": self.name,
            "status": "success",
            "data": infra_data,
        }


infrastructure_agent = InfrastructureAgent()
