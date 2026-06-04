"""FastAPI backend for the multi-agent travel planner.

This file defines the HTTP API, enables CORS, converts incoming JSON into the
LangGraph TravelState, executes the compiled workflow, and returns JSON output.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .graph import travel_graph
from .state import TravelState


app = FastAPI(title="Multi-Agent Travel Planner")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TripRequest(BaseModel):
    destination: str = Field(..., examples=["Goa"])
    days: int = Field(..., ge=1, examples=[4])
    budget: float = Field(..., ge=0, examples=[50000])
    travel_type: str = Field(..., examples=["family"])
    interests: list[str] = Field(default_factory=list, examples=[["beaches", "food"]])


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/generate-trip")
def generate_trip(request: TripRequest) -> dict:
    initial_state: TravelState = {
        "messages": [],
        "destination": request.destination,
        "days": request.days,
        "budget": request.budget,
        "travel_type": request.travel_type,
        "interests": request.interests,
    }

    try:
        result = travel_graph.invoke(initial_state)
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc

    return {
        "destination": result.get("destination"),
        "days": result.get("days"),
        "budget": result.get("budget"),
        "travel_type": result.get("travel_type"),
        "interests": result.get("interests", []),
        "itinerary": result.get("itinerary"),
        "weather": result.get("weather"),
        "hotels": result.get("hotels"),
        "transport": result.get("transport"),
        "budget_breakdown": result.get("budget_breakdown"),
        "final_report": result.get("final_report"),
    }
