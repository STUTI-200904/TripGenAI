export default function DestinationCard({
  image,
  title,
  location,
  price,
  setDestination,
}) {
  return (
    <div className="bg-zinc-900 rounded-3xl overflow-hidden hover:scale-105 transition duration-300">
      <img
        src={image}
        alt={title}
        className="w-full h-52 object-cover"
      />

      <div className="p-5">
        <h3 className="text-2xl font-semibold">{title}</h3>

        <p className="text-gray-400">{location}</p>

        <p className="text-orange-500 mt-2 font-semibold">
          {price}
        </p>

        <button
  onClick={() => setDestination(title)}
  className="mt-4 bg-orange-500 px-4 py-2 rounded-xl"
>
  Explore
</button>
      </div>
    </div>
  );
}