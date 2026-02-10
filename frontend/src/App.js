import React, { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ReferenceDot,
  ReferenceLine,
  ResponsiveContainer
} from "recharts";
import "./App.css";

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [changePoints, setChangePoints] = useState([]);

  const [startDate, setStartDate] = useState("2000-01-01");
  const [endDate, setEndDate] = useState("2023-12-31");

  const [showEvents, setShowEvents] = useState(true);
  const [showChangePoints, setShowChangePoints] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/prices")
      .then(res => res.json())
      .then(data =>
        setPrices(data.map(d => ({
          ...d,
          Date: new Date(d.Date).toISOString().slice(0, 10)
        })))
      );

    fetch("http://127.0.0.1:5000/api/events")
      .then(res => res.json())
      .then(data =>
        setEvents(data.map(d => ({
          ...d,
          Event_Date: new Date(d.Event_Date).toISOString().slice(0, 10)
        })))
      );

    fetch("http://127.0.0.1:5000/api/change-points")
      .then(res => res.json())
      .then(setChangePoints);
  }, []);

  const filteredPrices = prices.filter(
    p => p.Date >= startDate && p.Date <= endDate
  );

  const avgPrice =
    filteredPrices.reduce((sum, p) => sum + p.Price, 0) /
    (filteredPrices.length || 1);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Brent Oil Interactive Dashboard</h1>
      <p style={{ color: "#555" }}>
        Explore price trends, global events, and structural change points.
      </p>

      {/* Controls */}
      <div style={{ display: "flex", gap: "20px", marginBottom: "15px", flexWrap: "wrap" }}>
        <div>
          <label>Start Date</label><br />
          <input type="date" value={startDate} onChange={e => setStartDate(e.target.value)} />
        </div>
        <div>
          <label>End Date</label><br />
          <input type="date" value={endDate} onChange={e => setEndDate(e.target.value)} />
        </div>
        <div>
          <label>
            <input type="checkbox" checked={showEvents} onChange={() => setShowEvents(!showEvents)} />
            {" "}Show Events
          </label>
        </div>
        <div>
          <label>
            <input type="checkbox" checked={showChangePoints} onChange={() => setShowChangePoints(!showChangePoints)} />
            {" "}Show Change Points
          </label>
        </div>
      </div>

      {/* KPI Cards */}
      <div style={{ display: "flex", gap: "20px", marginBottom: "20px", flexWrap: "wrap" }}>
        <div className="card">Data Points<br /><strong>{filteredPrices.length}</strong></div>
        <div className="card">Average Price<br /><strong>${avgPrice.toFixed(2)}</strong></div>
        <div className="card">Events<br /><strong>{events.length}</strong></div>
      </div>

      {/* Chart */}
      <ResponsiveContainer width="100%" height={420}>
        <LineChart data={filteredPrices}>
          <CartesianGrid stroke="#eee" />
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="Price" stroke="#4f46e5" dot={false} />

          {/* Events */}
          {showEvents && events.map((e, i) => {
            const p = filteredPrices.find(d => d.Date === e.Event_Date)?.Price;
            if (!p) return null;
            return (
              <ReferenceDot
                key={i}
                x={e.Event_Date}
                y={p}
                r={5}
                fill="red"
                label={{ value: e.Event_Description, position: "top" }}
              />
            );
          })}

          {/* Change Points */}
          {showChangePoints && changePoints.map((cp, i) => (
            <ReferenceLine
              key={i}
              x={cp.date}
              stroke="orange"
              strokeDasharray="4 4"
              label={{ value: cp.label, position: "top" }}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default App;
