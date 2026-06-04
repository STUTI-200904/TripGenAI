from ..state import TravelState


def hotel_agent(state: TravelState) -> TravelState:
    destination = state.get("destination", "the destination")
    budget = state.get("budget", 0)
    travel_type = state.get("travel_type", "general")

    if budget < 20000:
        hotels = f"""
🏨 Recommended Budget Hotels in {destination}

1. Zostel {destination}
💰 ₹800 - ₹1500/night
⭐ Best for solo travelers and friends

2. FabHotel Prime
💰 ₹1500 - ₹2500/night
⭐ Budget-friendly with good amenities

3. Treebo Trend Hotel
💰 ₹2000 - ₹3000/night
⭐ Comfortable stay with breakfast
"""
    elif budget < 75000:
        hotels = f"""
🏨 Recommended Mid-Range Hotels in {destination}

1. BloomSuites {destination}
💰 ₹3500 - ₹5000/night
⭐ Great for {travel_type} trips

2. Fairfield by Marriott
💰 ₹4500 - ₹7000/night
⭐ Excellent comfort and location

3. Lemon Tree Hotel
💰 ₹4000 - ₹6500/night
⭐ Popular among families and groups
"""
    else:
        hotels = f"""
🏨 Luxury Stays in {destination}

1. Taj Resort
💰 ₹12000+/night
⭐ Premium luxury experience

2. Marriott Resort & Spa
💰 ₹15000+/night
⭐ Beachfront and luxury amenities

3. Hyatt Centric
💰 ₹10000+/night
⭐ High-end stay with premium services
"""

    return {"hotels": hotels}