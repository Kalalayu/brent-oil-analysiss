import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ReferenceDot, Legend } from 'recharts';
import './App.css';

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/prices')
      .then(res => res.json())
      .then(data => {
        const formatted = data.map(d => ({
          ...d,
          Date: new Date(d.Date).toISOString().slice(0,10) // ISO format
        }));
        setPrices(formatted);
      })
      .catch(err => console.error('Error fetching prices:', err));

    fetch('http://127.0.0.1:5000/api/events')
      .then(res => res.json())
      .then(data => {
        const formatted = data.map(d => ({
          ...d,
          Event_Date: new Date(d.Event_Date).toISOString().slice(0,10) // ISO format
        }));
        setEvents(formatted);
      })
      .catch(err => console.error('Error fetching events:', err));
  }, []);

  return (
    <div className="App" style={{ padding: '20px' }}>
      <h2>Brent Oil Prices with Key Events</h2>
      <LineChart width={900} height={450} data={prices}>
        <XAxis dataKey="Date" />
        <YAxis />
        <Tooltip />
        <CartesianGrid stroke="#ccc" />
        <Line type="monotone" dataKey="Price" stroke="#8884d8" />

        {/* Event markers */}
        {events.map((event, index) => {
          const priceAtEvent = prices.find(p => p.Date === event.Event_Date)?.Price;
          if (!priceAtEvent) return null; // skip if no matching price
          return (
            <ReferenceDot
              key={index}
              x={event.Event_Date}
              y={priceAtEvent}
              r={6}
              fill="red"
              stroke="none"
              label={{ position: 'top', value: event.Event_Description }}
            />
          );
        })}

        <Legend />
      </LineChart>
    </div>
  );
}

export default App;