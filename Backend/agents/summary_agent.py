"""Summary agent for producing the final trip report.

This agent combines the outputs from earlier graph nodes into one readable
report while preserving the structured fields already stored in TravelState.
"""

from langchain_core.messages import AIMessage

from ..state import TravelState


def _section(title: str, content: str | None) -> str:
    if not content:
        content = "Not available yet."
    return f"## {title}\n{content}"


def summary_agent(state: TravelState) -> TravelState:
    destination = state.get("destination", "your destination")
    days = state.get("days", 1)
    budget = state.get("budget", 0)
    travel_type = state.get("travel_type", "general")

    final_report = "\n\n".join(
        [
            f"# Final Trip Report: {destination}",
            (
                f"Trip overview: {days}-day {travel_type} trip to {destination} "
                f"with an estimated budget of {budget:,.2f}."
            ),
            _section("Day-wise Itinerary", state.get("itinerary")),
            _section("Weather Summary", state.get("weather")),
            _section("Hotel Recommendations", state.get("hotels")),
            _section("Transport Suggestions", state.get("transport")),
            _section("Budget Breakdown", state.get("budget_breakdown")),
        ]
    )

    return {
        "final_report": final_report,
        "messages": state.get("messages", []) + [AIMessage(content=final_report)],
    }
