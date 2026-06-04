"""Weather agent for adding destination weather to the travel plan.

This agent calls the OpenWeather API using OPENWEATHER_API_KEY from .env,
converts the raw weather response into a short traveler-friendly summary, and
returns a TravelState update for LangGraph to merge.
"""

import os
from typing import Any

import requests
from dotenv import load_dotenv

from ..state import TravelState


load_dotenv()

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def _get_api_key() -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENWEATHER_API_KEY is not set in your environment or .env file."
        )
    return api_key


def _fetch_weather(destination: str) -> dict[str, Any]:
    params = {
        "q": destination,
        "appid": _get_api_key(),
        "units": "metric",
    }

    try:
        response = requests.get(OPENWEATHER_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Unable to fetch weather for {destination}.") from exc

    data = response.json()
    if str(data.get("cod")) != "200":
        message = data.get("message", "Unknown OpenWeather API error.")
        raise RuntimeError(f"OpenWeather error for {destination}: {message}")

    return data


def _build_weather_summary(destination: str, weather_data: dict[str, Any]) -> str:
    weather = weather_data.get("weather", [{}])[0]
    main = weather_data.get("main", {})
    wind = weather_data.get("wind", {})

    description = weather.get("description", "Unavailable").title()
    temperature = main.get("temp", 0)
    feels_like = main.get("feels_like", 0)
    humidity = main.get("humidity", 0)
    wind_speed = wind.get("speed", 0)

    if temperature >= 30:
        tip = "Carry water, sunglasses, and light clothing."
    elif temperature >= 20:
        tip = "Comfortable weather for sightseeing."
    else:
        tip = "Carry a light jacket for outdoor activities."

    return f"""
🌤 Weather Snapshot - {destination}

🌡 Temperature: {temperature:.1f}°C
🤗 Feels Like: {feels_like:.1f}°C
☁ Condition: {description}
💧 Humidity: {humidity}%
💨 Wind Speed: {wind_speed} m/s

💡 Travel Tip:
{tip}
"""


def weather_agent(state: TravelState) -> TravelState:
    destination = state.get("destination", "the destination")
    weather_data = _fetch_weather(destination)

    return {
        "weather": _build_weather_summary(destination, weather_data),
    }
