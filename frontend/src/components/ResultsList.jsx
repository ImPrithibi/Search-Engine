import React from "react";

const ResultsList = ({ results }) => {
  if (!results || results.length === 0) {
    return <p className="text-center mt-5">No results found.</p>;
  }

  return (
    <div className="mt-5 px-10">
      {results.map((url, index) => (
        <div key={index} className="border-b py-2">
          <a href={url} target="_blank" rel="noopener noreferrer" className="text-blue-600 underline">
            {url}
          </a>
        </div>
      ))}
    </div>
  );
};

export default ResultsList;
