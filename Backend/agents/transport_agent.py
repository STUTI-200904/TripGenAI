from ..state import TravelState


def transport_agent(state: TravelState) -> TravelState:
    destination = state.get("destination", "your destination")
    travel_type = state.get("travel_type", "general").lower()

    if "couple" in travel_type:
        recommendation = "🚖 Private Cab + 🛵 Scooter Rental"
    elif "family" in travel_type:
        recommendation = "🚗 Self Drive Car + 🚖 Airport Cab"
    elif "solo" in travel_type:
        recommendation = "🛵 Scooter Rental + 🚕 App Cab"
    elif "friends" in travel_type:
        recommendation = "🛵 Scooter Rental + 🚗 Self Drive Car"
    else:
        recommendation = "🚖 Cab + Public Transport"

    transport = f"""
🚕 Smart Transport Guide - {destination}

🛵 Scooter Rental
💰 ₹400 - ₹700/day
✅ Best for local sightseeing

🚖 Local Cab / App Cab
💰 ₹150 - ₹500/trip
✅ Comfortable and convenient

🚗 Self Drive Car
💰 ₹1500 - ₹3000/day
✅ Best for long-distance travel

🚌 Public Transport
💰 ₹20 - ₹200/trip
✅ Budget-friendly option

⭐ AI Recommendation
{recommendation}
"""

    return {"transport": transport}