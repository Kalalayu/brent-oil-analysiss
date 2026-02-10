# Task 2 & 3 – Brent Oil Analysis and Dashboard
## Overview

Task 2: Data analysis of Brent oil prices with key global events. Explored trends, calculated correlations, and identified structural change points.

Task 3: Interactive dashboard to visualize analysis results using Flask backend and React + Recharts frontend.

## Backend Endpoints

/api/prices – Historical Brent prices

/api/events – Major events affecting prices

/api/change-points – Structural change points

# Setup

## Backend
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install flask pandas flask-cors
python app.py

## Frontend
cd frontend
npm install
npm start

# Future Enhancements

Automated change-point detection

Event category filters

Predictive modeling / price forecasting