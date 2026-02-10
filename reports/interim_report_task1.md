# Task 1: Brent Oil Analysis Documentation

## 1. Project Overview
**Brent Oil Analysis Project**  
This project analyzes historical Brent oil prices and explores how key events (geopolitical, economic, and political) influenced price movements. The goal is to provide stakeholders with actionable insights through data visualization and predictive analysis.

---

## 2. Objectives
- Collect and clean historical Brent oil price data.  
- Identify and document major events affecting prices.  
- Analyze trends, volatility, and correlations with events.  
- Prepare datasets for downstream analysis (Tasks 2 & 3).

---

## 3. Data Sources

| Dataset | Description | Source | Columns |
|---------|------------|--------|---------|
| `brent_prices.csv` | Historical Brent oil prices | Public datasets (EIA, Quandl) | Date, Price |
| `events.csv` | Key events affecting oil prices | News archives / Wikipedia | Event_Date, Event_Description, Category |

---

## 4. Methodology

### 4.1 Data Cleaning
- Parsed dates consistently (day-first format for historical data).  
- Sorted by date to maintain chronological order.  
- Handled missing values and duplicates.  

### 4.2 Data Analysis
- Computed basic statistics: min, max, mean, volatility.  
- Marked event dates for correlation with price trends.  
- Identified potential change points (e.g., financial crises, geopolitical shocks).  

### 4.3 Outputs for Task 2 & 3
- Clean CSV files ready for backend API.  
- JSON-ready structures for frontend visualization.

---

## 5. Observations / Insights
- Brent prices showed sharp drops during major economic shocks.  
- Geopolitical conflicts corresponded with sudden price spikes.  
- Volatility increases were often event-driven.  

---

## 6. Next Steps
- **Task 2**: Quantitative analysis and modeling (price forecasting, change-point detection).  
- **Task 3**: Interactive dashboard to visualize price trends and events.

---


