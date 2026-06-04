"""Hotel recommendation agent for the travel planner graph.

This agent uses destination, budget, and travel type from TravelState to create
three hotel recommendation tiers. It does not call a live booking API yet; it
returns useful category-level recommendations that can later be replaced with
real provider data.
"""

from ..state import TravelState


def _budget_context(budget: float) -> str:
    if budget <= 0:
        return "with flexible pricing"
    if budget < 20000:
        return "with strong value and low nightly rates"
    if budget < 75000:
        return "with a balanced comfort-to-cost ratio"
    return "with premium comfort and strong amenities"


def hotel_agent(state: TravelState) -> TravelState:
    destination = state.get("destination", "the destination")
    budget = state.get("budget", 0)
    travel_type = state.get("travel_type", "general")
    budget_context = _budget_context(budget)

    hotels = (
        f"Hotel recommendations for a {travel_type} trip to {destination} "
        f"{budget_context}:\n"
        f"- Budget hotel: Choose a clean guesthouse, hostel, or 2-star stay near "
        f"public transport and main attractions in {destination}.\n"
        f"- Mid-range hotel: Choose a 3-star boutique hotel or serviced apartment "
        f"with breakfast, good reviews, and easy access to sightseeing areas.\n"
        f"- Luxury hotel: Choose a 4-star or 5-star resort or premium hotel with "
        f"spacious rooms, concierge support, dining options, and reliable transport access."
    )

    return {"hotels": hotels}
