import React, { useState } from "react";
import axios from "axios";
import SearchBar from "./components/SearchBar";
import ResultsList from "./components/ResultsList";

function App() {
  const [results, setResults] = useState([]);

  const handleSearch = async (query) => {
    try {
      const response = await axios.get(`http://127.0.0.1:5001/search?q=${query}`);
      setResults(response.data.results);
    } catch (error) {
      console.error("Error fetching search results:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <h1 className="text-4xl text-center pt-10 font-bold">Search Engine</h1>
      <SearchBar onSearch={handleSearch} />
      <ResultsList results={results} />
    </div>
  );
}

export default App;
