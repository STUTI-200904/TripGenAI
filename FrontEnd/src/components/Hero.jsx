import { motion } from "framer-motion";

export default function Hero() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      className="grid grid-cols-2 gap-8 items-center"
    >
      <div>
        <p className="text-orange-500 uppercase tracking-widest text-sm">
          TripGenAI • AI Powered Travel Planner
        </p>

        <h1 className="text-6xl font-bold leading-tight mt-4">
          YOUR AI TRAVEL
          <br />
          COMPANION
        </h1>

        <p className="text-gray-400 mt-6 max-w-xl">
          Create personalized itineraries using multiple AI agents that handle
          budgeting, weather, hotels and transport.
        </p>
      </div>

      <img
        src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600"
        alt="Travel"
        className="w-full h-[300px] object-cover rounded-3xl"
      />
    </motion.div>
  );
}