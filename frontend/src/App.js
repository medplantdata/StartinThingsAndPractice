import './App.css';
import React, {useState} from 'react';
import { useNavigate } from "react-router-dom";


function App() {
  const[query,setQuery] = useState("");s
  const navigate =useNavigate();

  async function searchNP() {
    const res = await fetch("http://localhost:8000/api/search-np",{
      method: "POST",
      headers: {"content-Type": "application/json"},
      body: JSON. stringify({q:query}),
    });

  const data = await res.json(); 
  navigate("/results", { state: {query, data}});
  
}
  return (
    <div className="app">
      <h1 class = "main_heading">WAND<sup>3</sup></h1>
      <h2>Webtool for Acceleration of Neurological Disease Drug Discovery</h2>
      <h3>Search for plants, natural products, diseases, and drugs</h3>

      <div className="search-container">
        <input
          type="text"
          placeholder="Search..."
          className="search-input"
          value = {query}
          onChange={(e)=> setQuery(e.target.value)}
        />

        <div className="button-row">
          <button className="search-button">Search Plants</button>
          <button onClick = {searchNP} className="search-button">Search NP</button>
          <button className="search-button">Search Diseases</button>
          <button className="search-button">Search Drug Targets</button>
        </div>
      </div>
    </div>
  );
}

export default App;
