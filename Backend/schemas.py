"""Request and response schemas for the FastAPI boundary.

Pydantic models live here so API validation is separate from LangGraph state
and agent orchestration.
"""

from typing import Any

from pydantic import BaseModel, Field


class TripRequest(BaseModel):
    destination: str = Field(..., examples=["Goa"])
    days: int = Field(..., ge=1, examples=[4])
    budget: float = Field(..., ge=0, examples=[50000])
    travel_type: str = Field(..., examples=["family"])
    interests: list[str] = Field(default_factory=list, examples=[["beaches", "food"]])


class TripResponse(BaseModel):
    destination: str | None = None
    days: int | None = None
    budget: float | None = None
    travel_type: str | None = None
    interests: list[str] = Field(default_factory=list)
    itinerary: str | None = None
    weather: str | None = None
    hotels: str | None = None
    transport: str | None = None
    budget_breakdown: str | None = None
    final_report: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
