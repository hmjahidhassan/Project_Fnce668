# Project_Fnce668

This repository contains the files for the **Project_Fnce668** analysis. The project focuses on analyzing and visualizing financial data, specifically examining the relationships between oil prices, oil and non-oil companies' stock indices, and the S&P 500 index (SPX). This README outlines the purpose of each file in the repository.

## Files

### 1. `Price Data.xls`
This Excel file contains the main dataset used in the project. It includes historical prices for oil stocks, non-oil stocks, oil commodity prices (represented by `CL1 Comdty`), and the SPX index. The data is structured with dates as the index and price columns for each asset.

### 2. `Raw Price Data.xls`
This is the raw data file initially used for data preparation and cleaning. It includes unprocessed historical prices for the assets under analysis. The raw file provides the foundational data before any modifications or transformations are applied in the project.

### 3. `Term_Project_New.py`
This Python script performs the main analysis for the project. It includes the following steps:
   - **Data Loading**: Reads data from `Price Data.xls`.
   - **Data Processing**: Calculates daily returns for oil stocks, non-oil stocks, oil prices, and SPX.
   - **Index Creation**: Creates equal-weight indices for oil stocks and non-oil stocks.
   - **Regression Analysis**: Runs regression analysis on the oil index, non-oil index, and SPX index against oil price returns.
   - **Volatility Calculation**: Calculates and visualizes the 30-day rolling volatility for oil prices, oil index, and non-oil index.
   - **Cumulative Returns Calculation**: Calculates and visualizes cumulative returns for oil index, non-oil index, and oil prices.

### 4. `cumulative_returns_plot.png`
This image shows the cumulative returns for the oil company index, non-oil company index, and oil prices. The cumulative returns plot provides insight into the growth of each index over time, allowing for a comparison of performance between oil and non-oil companies relative to oil price changes.

### 5. `volatility_plot.png`
This image shows the 30-day rolling volatility for the oil company index, non-oil company index, and oil prices. The volatility plot helps in understanding the risk or volatility associated with oil prices and the two indices, highlighting periods of increased or decreased volatility.

### 6. `README.md`
This file provides an overview of the project, explaining the purpose of each file and the main steps involved in the analysis.
