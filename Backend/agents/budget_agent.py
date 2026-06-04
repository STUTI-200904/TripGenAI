"""Budget planning agent for estimated trip expenses.

This agent splits the user's total budget into practical travel categories and
returns a readable budget breakdown for the LangGraph state.
"""

from ..state import TravelState


def _format_money(amount: float) -> str:
    return f"{amount:,.2f}"


def budget_agent(state: TravelState) -> TravelState:
    budget = float(state.get("budget", 0))
    days = max(int(state.get("days", 1)), 1)
    destination = state.get("destination", "your destination")
    travel_type = state.get("travel_type", "general")

    hotel = budget * 0.40
    food = budget * 0.25
    transport = budget * 0.20
    activities = budget * 0.15
    per_day = budget / days

    budget_breakdown = (
        f"Estimated budget breakdown for a {days}-day {travel_type} trip to {destination}:\n"
        f"- Total budget: {_format_money(budget)}\n"
        f"- Daily average: {_format_money(per_day)} per day\n"
        f"- Hotel: {_format_money(hotel)} total, about {_format_money(hotel / days)} per day\n"
        f"- Food: {_format_money(food)} total, about {_format_money(food / days)} per day\n"
        f"- Transport: {_format_money(transport)} total, about {_format_money(transport / days)} per day\n"
        f"- Activities: {_format_money(activities)} total, about {_format_money(activities / days)} per day\n"
        "Use this as a planning estimate and adjust based on actual hotel rates, "
        "ticket prices, and seasonal demand."
    )

    return {"budget_breakdown": budget_breakdown}
