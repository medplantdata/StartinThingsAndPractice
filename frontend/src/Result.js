import React from "react";
import { useLocation } from "react-router-dom";

function Results() {
  const location = useLocation();
  const { query, data } = location.state || { query: "", data: null };

  if (!data) return <p>No results.</p>;

  return (
    <div>
      <h2>Results for: {query}</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default Results;