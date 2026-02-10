# backend/app.py
from flask import Flask, jsonify
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
    if not PRICES_PATH.exists():
        raise FileNotFoundError(f"Brent prices CSV not found: {PRICES_PATH}")
    df = pd.read_csv(PRICES_PATH, parse_dates=['Date'], dayfirst=True)
    df = df.sort_values('Date')
    return df

def load_events():
    if not EVENTS_PATH.exists():
        raise FileNotFoundError(f"Events CSV not found: {EVENTS_PATH}")
    df = pd.read_csv(EVENTS_PATH, parse_dates=['Event_Date'])
    df = df.sort_values('Event_Date')
    return df

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return "<h1>Brent Oil Analysis API</h1><p>Use /api/prices or /api/events</p>"

@app.route("/api/prices")
def api_prices():
    df = load_prices()
    return jsonify(df.to_dict(orient='records'))

@app.route("/api/events")
def api_events():
    df = load_events()
    return jsonify(df.to_dict(orient='records'))

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
