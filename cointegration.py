import pandas as pd
import yfinance as yf
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint
import matplotlib.pyplot as plt

'''



Ideal level of 100 sample pair:
less than - 3.3, p-value less than 0.05
Example:
Test Statistic: -4.0
P-value: 0.01
'''


# Define tickers and date range
tickers = ['AVGO', 'NVDA']
start_date = '2024-02-01'
end_date = '2025-02-21'

# Download adjusted closing prices
data = yf.download(tickers, start=start_date, end=end_date)
data = data['Close']
data = data.dropna()

# Run the Engle-Granger cointegration test
score, pvalue, _ = coint(data['AVGO'], data['NVDA'])
print(f"Cointegration test p-value: {pvalue:.4f}")

if pvalue < 0.05:
    print("The series are cointegrated")
else:
    print("The series are not cointegrated")

# Calculate the spread using a simple linear regression approach
# Regress AVGO on NVDA
X = sm.add_constant(data['NVDA'])
model = sm.OLS(data['AVGO'], X).fit()
print(model.summary())

# Compute the spread as the residuals from the regression
spread = data['AVGO'] - model.predict(X)

# Plot the spread
plt.figure(figsize=(10, 6))
plt.plot(spread, label='Spread')
plt.axhline(spread.mean(), color='red', linestyle='--', label='Mean')
plt.title('Spread between AVGO and NVDA')
plt.xlabel('Date')
plt.ylabel('Spread')
plt.legend()
plt.show()
pass


'''
test for
tickers = ['AVGO', 'NVDA']
start_date = '2024-02-01'
end_date = '2025-02-21'
is:  p-value of 0.6167 and the test statistic of -1.825
Not cointegrated
'''