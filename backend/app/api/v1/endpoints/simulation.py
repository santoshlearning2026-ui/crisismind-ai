"""Simulation endpoints."""

from fastapi import APIRouter

from app.api.v1.schemas.request import SimulationRequest
from app.utils.formatters import format_response

router = APIRouter()


@router.post("/simulate")
async def run_simulation(request: SimulationRequest) -> dict:
    """Run a risk simulation.
    
    Args:
        request: Simulation request
        
    Returns:
        Simulation response
    """
    return format_response(
        "success",
        data={
            "simulation_id": "sim_123",
            "city": request.city,
            "scenario": request.scenario,
            "status": "completed",
        },
    )
