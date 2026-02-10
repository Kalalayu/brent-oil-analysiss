// frontend/src/App.js
import React, { useEffect, useState } from "react";
import {
  LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid,
  ReferenceDot, Legend, ResponsiveContainer
} from "recharts";
import "./App.css";

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [categoryFilter, setCategoryFilter] = useState("All");

  // Fetch prices
  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/prices")
      .then(res => res.json())
      .then(data => {
        const formatted = data.map(d => ({
          ...d,
          Date: new Date(d.Date).toISOString().slice(0,10)
        }));
        setPrices(formatted);
      })
      .catch(err => console.error("Error fetching prices:", err));
  }, []);

  // Fetch events
  useEffect(() => {
    let url = "http://127.0.0.1:5000/api/events";
    if (categoryFilter !== "All") url += `?category=${categoryFilter}`;
    fetch(url)
      .then(res => res.json())
      .then(data => {
        const formatted = data.map(d => ({
          ...d,
          Event_Date: new Date(d.Event_Date).toISOString().slice(0,10)
        }));
        setEvents(formatted);
      })
      .catch(err => console.error("Error fetching events:", err));
  }, [categoryFilter]);

  const categories = ["All", "Geopolitical Conflict", "Economic Shock", "Political Instability"];

  return (
    <div className="App">
      <h2>Brent Oil Prices with Key Events</h2>

      {/* Filter */}
      <label>
        Filter Events by Category:{" "}
        <select value={categoryFilter} onChange={e => setCategoryFilter(e.target.value)}>
          {categories.map((c, i) => <option key={i} value={c}>{c}</option>)}
        </select>
      </label>

      {/* Responsive chart */}
      <ResponsiveContainer width="95%" height={500}>
        <LineChart data={prices} margin={{ top: 50, right: 50, left: 20, bottom: 50 }}>
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip />
          <CartesianGrid stroke="#ccc" />
          <Line type="monotone" dataKey="Price" stroke="#8884d8" />

          {/* Event markers */}
          {events.map((event, index) => {
            const priceAtEvent = prices.find(p => p.Date === event.Event_Date)?.Price;
            if (!priceAtEvent) return null;
            return (
              <ReferenceDot
                key={index}
                x={event.Event_Date}
                y={priceAtEvent}
                r={6}
                fill="red"
                stroke="none"
                label={{ position: "top", value: event.Event_Description }}
              />
            );
          })}

          <Legend />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default App;
