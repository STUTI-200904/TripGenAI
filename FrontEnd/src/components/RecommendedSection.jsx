import DestinationCard from "./DestinationCard";

export default function RecommendedSection({
  setDestination,
  setDays,
  setBudget,
  setTravelType,
  setInterests,
})  {
  const destinations = [
    {
      image:
        "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=600",
      title: "Bali",
  location: "Indonesia",
  price: "₹45,000",
  days: 4,
  travelType: "Couple",
  interests: "Beach",
    },
    {
      image:
        "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=600",
      title: "Tokyo",
  location: "Japan",
  price: "₹85,000",
  days: 6,
  travelType: "Solo",
  interests: "Technology",
    },
    {
      image:
        "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=600",
      title: "Dubai",
  location: "UAE",
  price: "₹70,000",
  days: 5,
  travelType: "Family",
  interests: "Shopping",
    },
    {
      image:
        "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600",
      title: "Paris",
  location: "France",
  price: "₹95,000",
  days: 5,
  travelType: "Couple",
  interests: "Sightseeing",
    },
  ];

  return (
    <div className="mt-14">
      <div className="flex justify-between items-end mb-6">
        <div>
          <h2 className="text-3xl font-bold">Recommended Destinations</h2>
          <p className="text-gray-400 mt-2">
            AI-picked destinations based on your travel preferences.
          </p>
        </div>

        <button className="text-orange-500 font-semibold">View all</button>
      </div>

      <div className="grid grid-cols-4 gap-6">
        {destinations.map((destination, index) => (
          <DestinationCard
  key={index}
  image={destination.image}
  title={destination.title}
  location={destination.location}
  price={destination.price}
  days={destination.days}
  travelType={destination.travelType}
  interests={destination.interests}
  setDestination={setDestination}
  setDays={setDays}
  setBudget={setBudget}
  setTravelType={setTravelType}
  setInterests={setInterests}
/>
        ))}
      </div>
    </div>
  );
}