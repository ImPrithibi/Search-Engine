import { useState } from "react";


function SearchBar({ onSearch }) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim() !== "") {
      onSearch(query);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex justify-center mt-10">
      <input
        type="text"
        placeholder="Search anything..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            onSearch(query);
          }
        }}
        className="border p-2 w-1/2 rounded-lg shadow"
      />
      <button
        type="submit"
        className="ml-2 bg-blue-500 text-white p-2 rounded-lg"
      >
        Search
      </button>
    </form>
  );
}

export default SearchBar;
