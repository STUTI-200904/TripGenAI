export default function AgentPanel() {
  return (
    <div className="bg-zinc-900 rounded-3xl p-6">
      <h2 className="text-2xl font-bold mb-4">AI Agents</h2>

      <div className="space-y-4 text-gray-300">
        <p> Planner Agent </p>
        <p>Weather Agent </p>
        <p> Hotel Agent </p>
        <p> Budget Agent </p>
        <p> Transport Agent </p>
      </div>
    </div>
  );
}