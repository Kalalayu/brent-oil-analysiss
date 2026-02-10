# backend/app.py
from flask import Flask, jsonify, request
import pandas as pd
from pathlib import Path
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# -----------------------------
# Paths to data
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
PRICES_PATH = BASE_DIR / "data" / "brent_prices.csv"
EVENTS_PATH = BASE_DIR / "data" / "events.csv"

# -----------------------------
# Load data
# -----------------------------
def load_prices():
    df = pd.read_csv(PRICES_PATH, parse_dates=['Date'], dayfirst=True)
    df = df.sort_values('Date')
    return df

def load_events():
    df = pd.read_csv(EVENTS_PATH, parse_dates=['Event_Date'])
    df = df.sort_values('Event_Date')
    return df

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return "<h1>Brent Oil Analysis API</h1><p>Use /api/prices, /api/events, or /api/change-points</p>"

@app.route("/api/prices")
def api_prices():
    df = load_prices()
    # Optional filtering by date range
    start = request.args.get('start')
    end = request.args.get('end')
    if start:
        df = df[df['Date'] >= start]
    if end:
        df = df[df['Date'] <= end]
    return jsonify(df.to_dict(orient='records'))

@app.route("/api/events")
def api_events():
    df = load_events()
    # Optional filtering by category
    category = request.args.get('category')
    if category:
        df = df[df['Category'].str.lower() == category.lower()]
    return jsonify(df.to_dict(orient='records'))

@app.route("/api/change-points")
def api_change_points():
    # Example Bayesian change points
    cps = [
        {"date": "2008-09-15", "reason": "Global Financial Crisis"},
        {"date": "2020-03-01", "reason": "COVID-19 shock"}
    ]
    return jsonify(cps)

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
