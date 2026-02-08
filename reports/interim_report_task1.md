# Interim Report – Task 1  
**Brent Oil Price Change Point Analysis**

## Overview
Task 1 establishes the analytical foundation for studying how major global events affect Brent crude oil prices. It focuses on data preparation, exploratory analysis, and event compilation to support later change point modeling and dashboard development.

## Data
- **Price Data:** Daily Brent oil prices (1987–2022)
- **Event Data:** 13 key geopolitical, economic, and policy events with dates and categories

## Methodology
- Cleaned and prepared time series data
- Conducted exploratory data analysis
- Computed log returns for volatility and stationarity assessment
- Structured event dataset for contextual analysis

## Key EDA Findings
- Prices show long-term trends and sharp spikes during major crises  
- Rolling averages reveal regime shifts  
- Log returns exhibit volatility clustering  
- Log returns appear stationary and suitable for change point modeling  

## Limitations
- Event dates are approximate  
- Multiple overlapping factors influence prices  
- Correlation does not imply causation  

## Next Steps
- **Task 2:** Apply Bayesian change point models to detect and quantify structural breaks and link them to events  
- **Task 3:** Develop an interactive dashboard using Flask and React to visualize prices, change points, and event impacts
