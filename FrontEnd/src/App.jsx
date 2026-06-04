import { useState } from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";

import RecommendedSection from "./components/RecommendedSection";
import AgentPanel from "./components/AgentPanel";
import TripSummary from "./components/TripSummary";

function App() {
  const [destination, setDestination] = useState("");

  return (
    <div className="min-h-screen bg-black text-white overflow-x-hidden">
      <Navbar />

      <main className="px-10 mt-10 max-w-[1500px] mx-auto">
        <Hero />

        

        <RecommendedSection
          setDestination={setDestination}
        />

        <div className="grid grid-cols-2 gap-6 mt-10 pb-10">
          <AgentPanel />

          <TripSummary
            destination={destination}
            setDestination={setDestination}
          />
        </div>
      </main>
    </div>
  );
}

export default App;