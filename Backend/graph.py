"""LangGraph workflow for the multi-agent travel planner.

This file wires the agents together in the required execution order and returns
a compiled graph that can be invoked by the FastAPI endpoint.
"""

from langchain_core.runnables import RunnableLambda
from langgraph.graph import END, START, StateGraph

from .agents.budget_agent import budget_agent
from .agents.hotel_agent import hotel_agent
from .agents.planner_agent import planner_agent
from .agents.summary_agent import summary_agent
from .agents.transport_agent import transport_agent
from .agents.weather_agent import weather_agent
from .state import TravelState


def create_travel_graph():
    workflow = StateGraph(TravelState)

    workflow.add_node("planner", RunnableLambda(planner_agent))
    workflow.add_node("weather", RunnableLambda(weather_agent))
    workflow.add_node("hotel", RunnableLambda(hotel_agent))
    workflow.add_node("budget", RunnableLambda(budget_agent))
    workflow.add_node("transport", RunnableLambda(transport_agent))
    workflow.add_node("summary", RunnableLambda(summary_agent))

    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "weather")
    workflow.add_edge("weather", "hotel")
    workflow.add_edge("hotel", "budget")
    workflow.add_edge("budget", "transport")
    workflow.add_edge("transport", "summary")
    workflow.add_edge("summary", END)

    return workflow.compile()


travel_graph = create_travel_graph()
