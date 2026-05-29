# Task 2 - Stock Price Prediction

## Task Objective
- Predict the next day\'s Close price from historical stock data.
- Use Open, High, Low, and Volume as input features.
- Compare regression models and visualize actual versus predicted prices.

## Dataset Used
- Historical stock data downloaded with yfinance.
- Example ticker used in the notebook: AAPL.
- Features: Open, High, Low, Volume.
- Target: next day\'s Close price created with a shifted Close column.

## Models Applied
- Linear Regression
- Random Forest Regressor

## Key Results and Findings
- Linear Regression performed best on the test split with MSE 21.1051 and R2 0.9220.
- Random Forest Regressor performed weaker here with MSE 86.9174 and R2 0.6786.
- The next day Close prediction was about 310.97 from Linear Regression and 281.36 from Random Forest, while the actual value was about 312.51.
- The time-ordered split was important because shuffling would break the stock forecasting setup.
