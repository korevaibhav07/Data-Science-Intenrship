# Task 8 – Sales Forecasting & Trend Analysis

## Objective
The objective of this task is to analyze historical sales data, identify sales trends over time, and predict future sales using basic time-series forecasting techniques.

## Dataset
- **sales_data.csv** (from previous task)
  - Contains transactional sales records including order date, quantity, unit price, and revenue.

## Work Done
1. Loaded historical sales data.
2. Converted order dates into datetime format.
3. Calculated total revenue per day to create time-series data.
4. Analyzed sales trends using line plots and rolling averages.
5. Applied basic forecasting techniques:
   - Moving Average Forecast
   - Linear Regression Trend Forecast
6. Evaluated forecasting accuracy using Mean Absolute Error (MAE).
7. Predicted sales for the next 7 days.
8. Saved all intermediate and final outputs for reuse and analysis.

## Output Files
- **daily_sales.csv** – Aggregated daily revenue data.
- **forecast_test.csv** – Actual vs predicted revenue for evaluation.
- **forecast_next7days.csv** – Predicted future sales values.
- **plots/sales_trend.png** – Daily sales trend visualization.
- **plots/forecast_vs_actual.png** – Actual vs forecast comparison plot.

## Conclusion
This task demonstrates how historical sales data can be transformed into time-series format to analyze trends and forecast future revenue. Such forecasting helps businesses in planning, inventory management, and decision-making.


