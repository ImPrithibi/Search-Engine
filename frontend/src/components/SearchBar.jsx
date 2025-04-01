import React, { useState } from "react";

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState("");

  const handleSearch = (e) => {
    e.preventDefault();
    if (query.trim() === "") return;
    onSearch(query);
  };

  return (
    <form onSubmit={handleSearch} className="flex justify-center mt-10">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search something..."
        className="border border-gray-400 p-2 w-1/2 rounded-l"
      />
      <button
        type="submit"
        className="bg-blue-500 text-white px-4 rounded-r"
      >
        Search
      </button>
    </form>
  );
};

export default SearchBar;
