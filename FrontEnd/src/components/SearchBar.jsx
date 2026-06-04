import { Search } from "lucide-react";

export default function SearchBar() {
  return (
    <div className="mt-10">
      <div className="flex items-center bg-zinc-900 rounded-2xl p-4">
        <Search className="text-orange-500" />

        <input
          type="text"
          placeholder="Search destination..."
          className="ml-4 bg-transparent w-full outline-none text-white"
        />
      </div>
    </div>
  );
}