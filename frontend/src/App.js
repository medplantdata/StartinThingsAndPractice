import logo from './logo.svg';
import './App.css';
import React from 'react';

function App() {
  return (
    <div className="app">
      <h1>WAND3</h1>
      <h2>Webtool for Acceleration of Neurological Disease Drug Discovery</h2>
      <h3>Search for plants, natural products, diseases, and drugs</h3>

      <div className="search-container">
        <input
          type="text"
          placeholder="Search..."
          className="search-input"
        />

        <div className="button-row">
          <button className="search-button">Search Plants</button>
          <button className="search-button">Search NP</button>
          <button className="search-button">Search Diseases</button>
          <button className="search-button">Search Drugs</button>
        </div>
      </div>
    </div>
  );
}

export default App;
