from ..state import TravelState


def _format_money(amount: float) -> str:
    return f"₹{amount:,.0f}"


def budget_agent(state: TravelState) -> TravelState:
    budget = float(state.get("budget", 0))
    days = max(int(state.get("days", 1)), 1)

    hotel = budget * 0.40
    food = budget * 0.25
    transport = budget * 0.20
    activities = budget * 0.15
    per_day = budget / days

    budget_breakdown = f"""
💰 Budget Analytics

💵 Total Budget
{_format_money(budget)}

📅 Daily Budget
{_format_money(per_day)} / day

━━━━━━━━━━━━━━

🏨 Hotel
{_format_money(hotel)}

🍴 Food
{_format_money(food)}

🚕 Transport
{_format_money(transport)}

🎯 Activities
{_format_money(activities)}

━━━━━━━━━━━━━━

✅ Budget Status
Well balanced allocation for the trip.
"""

    return {"budget_breakdown": budget_breakdown}