import DestinationCard from "./DestinationCard";

export default function RecommendedSection() {
  const destinations = [
    {
      image:
        "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=600",
      title: "Bali",
      location: "Indonesia",
      price: "₹45,000",
    },
    {
      image:
        "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=600",
      title: "Tokyo",
      location: "Japan",
      price: "₹85,000",
    },
    {
      image:
        "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=600",
      title: "Dubai",
      location: "UAE",
      price: "₹70,000",
    },
    {
      image:
        "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600",
      title: "Paris",
      location: "France",
      price: "₹95,000",
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
          />
        ))}
      </div>
    </div>
  );
}