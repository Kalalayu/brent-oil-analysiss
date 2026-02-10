from flask import Flask, jsonify
import pandas as pd
from pathlib import Path
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
PRICES_PATH = BASE_DIR / "data" / "brent_prices.csv"
EVENTS_PATH = BASE_DIR / "data" / "events.csv"

# -----------------------------
# Load & cache data
# -----------------------------
prices_df = pd.read_csv(PRICES_PATH, parse_dates=["Date"]).sort_values("Date")
events_df = pd.read_csv(EVENTS_PATH, parse_dates=["Event_Date"]).sort_values("Event_Date")

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return "<h2>Brent Oil Analysis API</h2><p>Use /api/prices, /api/events, /api/change-points</p>"

@app.route("/api/prices")
def prices():
    return jsonify(prices_df.to_dict(orient="records"))

@app.route("/api/events")
def events():
    return jsonify(events_df.to_dict(orient="records"))

@app.route("/api/change-points")
def change_points():
    return jsonify([
        {"date": "2008-09-15", "label": "Global Financial Crisis"},
        {"date": "2020-03-01", "label": "COVID-19 Shock"}
    ])

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
