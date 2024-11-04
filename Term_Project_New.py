import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load the Excel file and the 'Data' sheet
file_path = 'Price Data.xls'
data = pd.read_excel(file_path, sheet_name='Data', parse_dates=['Date'], index_col='Date', engine='xlrd')

# Define columns for oil stocks, non-oil stocks, oil price, and SPX index
oil_stocks_columns = ['XOM US Equity', 'CVX US Equity', 'COP US Equity', 'EOG US Equity', 
                      'WMB US Equity', 'SLB US Equity', 'OKE US Equity', 'PSX US Equity', 
                      'KMI US Equity', 'FANG US Equity', 'MPC US Equity']
non_oil_stocks_columns = ['AAPL US Equity', 'NVDA US Equity', 'MSFT US Equity', 'GOOGL US Equity', 
                          'AMZN US Equity', 'META US Equity', 'BRK/B US Equity', 'LLY US Equity', 
                          'AVGO US Equity']
oil_price_column = 'CL1 Comdty'
spx_column = 'SPX'

# Split the data into respective categories
oil_stocks = data[oil_stocks_columns]
non_oil_stocks = data[non_oil_stocks_columns]
oil_prices = data[[oil_price_column]]
spx_index = data[[spx_column]]

# Calculate daily returns for oil stocks, non-oil stocks, oil prices, and SPX index
oil_stocks_returns = oil_stocks.pct_change().dropna()
non_oil_stocks_returns = non_oil_stocks.pct_change().dropna()
oil_prices_returns = oil_prices.pct_change().dropna()
spx_returns = spx_index.pct_change().dropna()

# Create equal-weighted indices for oil and non-oil stocks
oil_index = oil_stocks_returns.mean(axis=1)
non_oil_index = non_oil_stocks_returns.mean(axis=1)

# Define a function to run the OLS regression
def run_regression(index_returns, oil_price_returns):
    X = sm.add_constant(oil_price_returns)  # Add a constant to the independent variable
    model = sm.OLS(index_returns, X)        # Define the OLS model
    results = model.fit()                   # Fit the model
    return results

# Run regression for oil company and non-oil company indices against oil price returns
oil_index_regression = run_regression(oil_index, oil_prices_returns[oil_price_column])
non_oil_index_regression = run_regression(non_oil_index, oil_prices_returns[oil_price_column])

print("Regression results for Oil Company Index:")
print(oil_index_regression.summary())

print("\nRegression results for Non-Oil Company Index:")
print(non_oil_index_regression.summary())

# Align the SPX index returns with oil price returns and run regression
combined_data = pd.concat([spx_returns, oil_prices_returns[oil_price_column]], axis=1).dropna()
aligned_spx_returns = combined_data[spx_column]
aligned_oil_price_returns = combined_data[oil_price_column]

spx_index_regression = run_regression(aligned_spx_returns, aligned_oil_price_returns)
print("\nRegression results for SPX Index:")
print(spx_index_regression.summary())

# Calculate rolling 30-day volatility (standard deviation)
oil_index_volatility = oil_index.rolling(window=30).std()
non_oil_index_volatility = non_oil_index.rolling(window=30).std()
oil_price_volatility = oil_prices_returns[oil_price_column].rolling(window=30).std()

# Plot 30-day rolling volatility
plt.figure(figsize=(10, 6))
plt.plot(oil_index_volatility, label='Oil Company Index Volatility', color='blue')
plt.plot(non_oil_index_volatility, label='Non-Oil Company Index Volatility', color='green')
plt.plot(oil_price_volatility, label='Oil Price Volatility', color='red', linestyle='--')
plt.title('30-Day Rolling Volatility: Oil Company, Non-Oil Company, and Oil Prices')
plt.xlabel('Date')
plt.ylabel('Volatility (Standard Deviation)')
plt.legend()
plt.grid(True)
plt.savefig("volatility_plot.png")  # Save as an image file
plt.close()

# Calculate cumulative returns for oil and non-oil indices and oil prices
cumulative_oil_index = (1 + oil_index).cumprod() - 1
cumulative_non_oil_index = (1 + non_oil_index).cumprod() - 1
cumulative_oil_prices = (1 + oil_prices_returns[oil_price_column]).cumprod() - 1

# Plot cumulative returns
plt.figure(figsize=(10, 6))
plt.plot(cumulative_oil_index, label='Oil Company Index Cumulative Returns', color='blue')
plt.plot(cumulative_non_oil_index, label='Non-Oil Company Index Cumulative Returns', color='green')
plt.plot(cumulative_oil_prices, label='Oil Price Cumulative Returns', color='red', linestyle='--')
plt.title('Cumulative Returns: Oil Company, Non-Oil Company, and Oil Prices')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.savefig("cumulative_returns_plot.png")  # Save as an image file
plt.close()
