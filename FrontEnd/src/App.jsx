import { useState } from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";

import RecommendedSection from "./components/RecommendedSection";
import AgentPanel from "./components/AgentPanel";
import TripSummary from "./components/TripSummary";

function App() {
  const [destination, setDestination] = useState("");
  const [days, setDays] = useState("");
  const [budget, setBudget] = useState("");
  const [travelType, setTravelType] = useState("");
  const [interests, setInterests] = useState("");
  const [tripGenerated, setTripGenerated] = useState(false);

  return (
    <div className="min-h-screen bg-black text-white overflow-x-hidden">
      <Navbar />

      <main className="px-10 mt-10 max-w-[1500px] mx-auto">
        <Hero />

        

        <RecommendedSection
  setDestination={setDestination}
  setDays={setDays}
  setBudget={setBudget}
  setTravelType={setTravelType}
  setInterests={setInterests}
/>

        <div className="grid grid-cols-2 gap-6 mt-10 pb-10">
          <AgentPanel tripGenerated={tripGenerated} />

          <TripSummary
  destination={destination}
  setDestination={setDestination}
  days={days}
  setDays={setDays}
  budget={budget}
  setBudget={setBudget}
  travelType={travelType}
  setTravelType={setTravelType}
  interests={interests}
  setInterests={setInterests}
  setTripGenerated={setTripGenerated}
/>
        </div>
      </main>
    </div>
  );
}

export default App;