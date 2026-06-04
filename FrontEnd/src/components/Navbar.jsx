export default function Navbar() {
  return (
    <div className="flex justify-between items-center px-10 py-6">
      <h1 className="text-3xl font-bold">
        Trip<span className="text-orange-500">GenAI</span>
      </h1>

      <div className="flex gap-8 text-gray-400">
        <p>Home</p>
        <p>Trips</p>
        <p>Bookings</p>
        <p>Profile</p>
      </div>
    </div>
  );
}