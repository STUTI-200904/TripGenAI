"""Planner agent for generating a day-wise travel itinerary.

This agent is responsible only for itinerary generation. It reads trip inputs
from TravelState, calls ChatGroq through LangChain, and returns updated state
fields for LangGraph to merge into the workflow state.
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from ..state import TravelState


load_dotenv()


itinerary_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert travel planner. Create a clear day-wise itinerary. "
            "Use the destination, trip length, budget, travel type, and interests. "
            "Keep the plan practical, organized, and suitable for the user's style.",
        ),
        (
            "human",
            "Destination: {destination}\n"
            "Days: {days}\n"
            "Budget: {budget}\n"
            "Travel type: {travel_type}\n"
            "Interests: {interests}\n\n"
            "Generate a day-wise itinerary with morning, afternoon, and evening plans. "
            "Include budget-aware suggestions where useful.",
        ),
    ]
)


def get_llm() -> ChatGroq:
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise RuntimeError("GROQ_API_KEY is not set in your environment or .env file.")

    return ChatGroq(
        groq_api_key=groq_api_key,
        model_name=os.getenv("GROQ_MODEL_NAME", "llama-3.3-70b-versatile"),
        temperature=float(os.getenv("GROQ_TEMPERATURE", "0")),
    )


def planner_agent(state: TravelState) -> TravelState:
    destination = state.get("destination", "the destination")
    days = state.get("days", 1)
    budget = state.get("budget", 0)
    travel_type = state.get("travel_type", "general")
    interests = state.get("interests") or ["general sightseeing"]
    interests_text = ", ".join(interests)

    prompt = itinerary_prompt.format_prompt(
        destination=destination,
        days=days,
        budget=budget,
        travel_type=travel_type,
        interests=interests_text,
    )
    response = get_llm().invoke(prompt)

    user_message = (
        f"Create a {days}-day {travel_type} itinerary for {destination} "
        f"within a budget of {budget}. Interests: {interests_text}."
    )

    return {
        "itinerary": response.content,
        "messages": state.get("messages", [])
        + [
            HumanMessage(content=user_message),
            AIMessage(content=response.content),
        ],
    }
