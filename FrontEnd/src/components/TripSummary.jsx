import { useState } from "react";
import axios from "axios";

export default function TripSummary({
  destination,
  setDestination,
})  {
  
  const [days, setDays] = useState("");
  const [budget, setBudget] = useState("");
  const [travelType, setTravelType] = useState("");
  const [interests, setInterests] = useState("");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateTrip = async () => {
    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/generate-trip",
        {
          destination: destination,
          days: Number(days),
          budget: Number(budget),
          travel_type: travelType,
          interests: interests
            .split(",")
            .map((item) => item.trim())
            .filter(Boolean),
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to generate trip");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-zinc-900 rounded-3xl p-6">
      <h2 className="text-2xl font-bold mb-4 text-orange-400">
  ✈️ Trip Planner
</h2>

      <div className="space-y-3">
        <input
          className="w-full p-3 rounded-xl bg-zinc-800 text-white"
          placeholder="Destination"
          value={destination}
          onChange={(e) => setDestination(e.target.value)}
        />

        <input
          className="w-full p-3 rounded-xl bg-zinc-800 text-white"
          placeholder="Days"
          type="number"
          value={days}
          onChange={(e) => setDays(e.target.value)}
        />

        <input
          className="w-full p-3 rounded-xl bg-zinc-800 text-white"
          placeholder="Budget"
          type="number"
          value={budget}
          onChange={(e) => setBudget(e.target.value)}
        />

        <input
          className="w-full p-3 rounded-xl bg-zinc-800 text-white"
          placeholder="Travel Type"
          value={travelType}
          onChange={(e) => setTravelType(e.target.value)}
        />

        <input
          className="w-full p-3 rounded-xl bg-zinc-800 text-white"
          placeholder="Interests (comma separated)"
          value={interests}
          onChange={(e) => setInterests(e.target.value)}
        />
      </div>

      <button
        onClick={generateTrip}
        className="mt-6 bg-orange-500 px-5 py-3 rounded-xl w-full"
      >
        {loading ? "Generating..." : "Generate Plan"}
      </button>

      {result && (
  <div className="mt-6 space-y-6">
    <div className="bg-orange-500 text-black p-5 rounded-2xl">
  <h3 className="text-2xl font-bold mb-2">
    📍 {result.destination}
  </h3>

  <div className="grid grid-cols-2 gap-2 text-sm font-semibold">
    <p>📅 {result.days} Days</p>
    <p>💰 ₹{result.budget}</p>
    <p>✈️ {result.travel_type}</p>
    <p>🎯 {result.interests?.join(", ")}</p>
  </div>
</div>

    <div className="bg-zinc-800 p-5 rounded-2xl border border-zinc-700">
      <h3 className="font-bold text-orange-400 mb-2">🌦 Weather</h3>
      <div className="whitespace-pre-wrap text-gray-300 text-sm">
  {result.weather}
</div>
    </div>

    <div className="bg-zinc-800 p-5 rounded-2xl border border-zinc-700">
      <h3 className="font-bold text-orange-400 mb-2">🏨 Hotels</h3>
      <div className="whitespace-pre-wrap text-gray-300 text-sm">
  {result.hotels}
</div>
    </div>

    <div className="bg-zinc-800 p-5 rounded-2xl border border-zinc-700">
      <h3 className="font-bold text-orange-400 mb-2">🚕 Transport</h3>
      <div className="whitespace-pre-wrap text-gray-300 text-sm">
  {result.transport}
</div>
    </div>

    <div className="bg-zinc-800 p-5 rounded-2xl border border-zinc-700">
      <h3 className="font-bold text-orange-400 mb-2">
        💰 Budget Breakdown
      </h3>
      <div className="whitespace-pre-wrap text-gray-300 text-sm">
  {result.budget_breakdown}
</div>
    </div>

    <div className="bg-zinc-800 p-4 rounded-xl max-h-[500px] overflow-y-auto">
      <h3 className="font-bold text-orange-400 mb-2">🗓 Itinerary</h3>
      <pre className="whitespace-pre-wrap text-gray-300 text-sm">
        {result.itinerary}
      </pre>
    </div>

    

  </div>
)}
      
    </div>
  );
}