"""Risk prediction service."""

import logging
from typing import Dict, Any

from app.models.ml.flood_risk_model import flood_risk_model
from app.models.ml.heatwave_risk_model import heatwave_risk_model
from app.models.ml.outage_risk_model import outage_risk_model

logger = logging.getLogger(__name__)


class RiskService:
    """Risk prediction service."""

    async def predict_flood_risk(self, city: str, features: Dict[str, float]) -> Dict[str, Any]:
        """Predict flood risk.
        
        Args:
            city: City name
            features: Input features
            
        Returns:
            Risk prediction
        """
        logger.info(f"Predicting flood risk for {city}")
        prediction = flood_risk_model.predict(features)
        return {"city": city, "risk_type": "flood", **prediction}

    async def predict_heatwave_risk(self, city: str, features: Dict[str, float]) -> Dict[str, Any]:
        """Predict heatwave risk.
        
        Args:
            city: City name
            features: Input features
            
        Returns:
            Risk prediction
        """
        logger.info(f"Predicting heatwave risk for {city}")
        prediction = heatwave_risk_model.predict(features)
        return {"city": city, "risk_type": "heatwave", **prediction}

    async def predict_outage_risk(self, city: str, features: Dict[str, float]) -> Dict[str, Any]:
        """Predict power outage risk.
        
        Args:
            city: City name
            features: Input features
            
        Returns:
            Risk prediction
        """
        logger.info(f"Predicting outage risk for {city}")
        prediction = outage_risk_model.predict(features)
        return {"city": city, "risk_type": "power_outage", **prediction}

    async def get_all_risks(self, city: str, features: Dict[str, float]) -> Dict[str, Any]:
        """Get all risk predictions for city.
        
        Args:
            city: City name
            features: Input features
            
        Returns:
            All risk predictions
        """
        logger.info(f"Predicting all risks for {city}")
        predictions = await Promise.all([
            self.predict_flood_risk(city, features),
            self.predict_heatwave_risk(city, features),
            self.predict_outage_risk(city, features),
        ])
        return {"city": city, "predictions": predictions}


risk_service = RiskService()
