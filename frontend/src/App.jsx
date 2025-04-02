import { useState } from "react";
import axios from "axios";
import SearchBar from "./components/SearchBar";
import ResultsList from "./components/ResultsList";

function App() {
  const [results, setResults] = useState([]);
  const [message, setMessage] = useState("");

  const handleSearch = async (query) => {
    setMessage("Searching…");
    setResults([]);

    try {
      const response = await axios.get(`/api/search?q=${query}`);
      
      if (response.data.crawled && response.data.crawled.length > 0) {
        setMessage(`Searching done. Found these fresh pages for '${query}'`);
        setResults(response.data.crawled);
      } else if (response.data.results && response.data.results.length > 0) {
        setMessage(`Results fetched from index for '${query}'`);
        setResults(response.data.results);
      } else {
        setMessage(`No results found for '${query}'.`);
      }

    } catch (error) {
      setMessage("Error fetching search results.");
      console.error("Search error:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <h1 className="text-4xl text-center pt-10 font-bold">Search Engine</h1>
      <SearchBar onSearch={handleSearch} />
      <p className="text-center mt-4 text-gray-700">{message}</p>
      <ResultsList results={results} />
    </div>
  );
}

export default App;
