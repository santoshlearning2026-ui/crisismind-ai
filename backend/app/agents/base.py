"""Base agent class."""

import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Base agent class."""

    def __init__(self, name: str, description: str):
        """Initialize agent.
        
        Args:
            name: Agent name
            description: Agent description
        """
        self.name = name
        self.description = description
        self.state = {}

    @abstractmethod
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute agent.
        
        Args:
            input_data: Input data
            
        Returns:
            Execution result
        """
        pass

    async def initialize(self) -> None:
        """Initialize agent resources."""
        logger.info(f"Initializing agent: {self.name}")

    async def shutdown(self) -> None:
        """Shutdown agent resources."""
        logger.info(f"Shutting down agent: {self.name}")

    def set_state(self, key: str, value: Any) -> None:
        """Set agent state.
        
        Args:
            key: State key
            value: State value
        """
        self.state[key] = value

    def get_state(self, key: str, default: Optional[Any] = None) -> Any:
        """Get agent state.
        
        Args:
            key: State key
            default: Default value
            
        Returns:
            State value
        """
        return self.state.get(key, default)
