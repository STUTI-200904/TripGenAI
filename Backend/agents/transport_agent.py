"""Transport recommendation agent for the travel planner graph.

This agent suggests practical airport, local, public transport, and taxi
options based on the destination and travel type in TravelState.
"""

from ..state import TravelState


def _travel_type_tip(travel_type: str) -> str:
    normalized = travel_type.lower()
    if "family" in normalized:
        return "Prioritize comfort, luggage space, and pre-booked transfers."
    if "solo" in normalized:
        return "Prioritize flexible routes, safe pickup points, and verified operators."
    if "couple" in normalized:
        return "Prioritize convenience, scenic routes, and private transfers for late evenings."
    if "business" in normalized:
        return "Prioritize reliability, shorter wait times, and app-based receipts."
    return "Balance cost, convenience, and safety while choosing transport."


def transport_agent(state: TravelState) -> TravelState:
    destination = state.get("destination", "your destination")
    travel_type = state.get("travel_type", "general")
    tip = _travel_type_tip(travel_type)

    transport = (
        f"Transport suggestions for a {travel_type} trip to {destination}:\n"
        f"- Airport transport: Use airport prepaid taxis, app-based cabs, or a "
        f"pre-booked hotel transfer for arrival and departure.\n"
        f"- Local transport: Use rental scooters, rental cars, hotel shuttles, or "
        f"guided day-trip vehicles depending on comfort and distance.\n"
        f"- Public transport: Check local buses, metro, trains, ferries, or shared "
        f"vans where available for budget-friendly movement around {destination}.\n"
        f"- Taxi options: Use app-based taxis where supported, local licensed taxis, "
        f"or full-day cab rentals for sightseeing.\n"
        f"- Travel type tip: {tip}"
    )

    return {"transport": transport}
