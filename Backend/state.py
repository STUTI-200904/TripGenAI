"""Shared LangGraph state definition for the travel planner workflow."""

from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, HumanMessage


class TravelState(TypedDict, total=False):
    destination: str
    days: int
    budget: float
    travel_type: str
    interests: list[str]

    itinerary: str
    weather: str
    hotels: str
    transport: str
    budget_breakdown: str
    final_report: str

    messages: Annotated[list[HumanMessage | AIMessage], "Conversation history"]
