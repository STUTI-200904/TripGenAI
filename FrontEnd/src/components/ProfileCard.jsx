export default function ProfileCard() {
  return (
    <div className="bg-zinc-900 rounded-3xl p-6 h-full">
      <h2 className="text-2xl font-bold text-orange-500">
        Traveler Profile
      </h2>

      <p className="text-gray-400 mt-3">
        AI Travel Explorer
      </p>

      <div className="mt-6 space-y-3 text-gray-300">
        <p>Trips Planned: 12</p>
        <p>Countries: 8</p>
        <p>Budget Saved: ₹85,000</p>
      </div>
    </div>
  );
}