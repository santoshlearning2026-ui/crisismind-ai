"""Orchestrator agent using LangGraph."""

import logging
from typing import Dict, Any

from app.agents.base import BaseAgent
from app.agents.weather_agent import weather_agent
from app.agents.infrastructure_agent import infrastructure_agent
from app.agents.news_agent import news_agent
from app.agents.prediction_agent import prediction_agent
from app.agents.recommendation_agent import recommendation_agent

logger = logging.getLogger(__name__)


class OrchestratorAgent(BaseAgent):
    """Orchestrator agent coordinates all other agents using LangGraph."""

    def __init__(self):
        """Initialize orchestrator agent."""
        super().__init__(
            name="OrchestratorAgent",
            description="Coordinates all agents in the risk prediction workflow",
        )
        self.agents = [
            weather_agent,
            infrastructure_agent,
            news_agent,
            prediction_agent,
            recommendation_agent,
        ]

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute orchestrator workflow.
        
        Args:
            input_data: Input data with city name
            
        Returns:
            Complete risk assessment
        """
        city = input_data.get("city")
        logger.info(f"Orchestrator starting workflow for: {city}")
        
        results = {"city": city, "agents": {}}
        
        # Execute agents in sequence
        for agent in self.agents:
            try:
                agent_result = await agent.execute(input_data)
                results["agents"][agent.name] = agent_result
                logger.info(f"{agent.name} completed successfully")
            except Exception as e:
                logger.error(f"{agent.name} failed: {e}")
                results["agents"][agent.name] = {
                    "status": "failed",
                    "error": str(e),
                }
        
        return {
            "agent": self.name,
            "status": "success",
            "data": results,
        }


orchestrator_agent = OrchestratorAgent()
