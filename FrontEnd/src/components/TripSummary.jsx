export default function TripSummary() {
  return (
    <div className="bg-zinc-900 rounded-3xl p-6">
      <h2 className="text-2xl font-bold mb-4">Trip Summary</h2>

      <div className="space-y-3 text-gray-300">
        <p>Destination : Bali</p>
        <p>Days : 6</p>
        <p>Budget : ₹50,000</p>
      </div>

      <button className="mt-6 bg-orange-500 px-5 py-3 rounded-xl">
        Generate Plan
      </button>
    </div>
  );
}