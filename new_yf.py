import pandas as pd
import yfinance as yf
import datetime


def get_data(tic_list, start_date, end_date):
    data = yf.download(tic_list, start=start_date, end=end_date)
    return data

def test():
    symbols = ['AAPL', 'GOOGL']
    start_date = '2024-11-01'
    end_date = '2025-02-21'
    data_by_symbol = get_data_by_list(symbols, start_date, end_date)
    
    for symbol, df_single in data_by_symbol.items():
        print(f"\nPrice data for {symbol}:")
        print(df_single.head())

def get_data_by_list(symbols:list, start_date, end_date)->dict:
    data = get_data(symbols, start_date, end_date)
    #data = yf.download(symbols, period="1mo")
    data_by_symbol = {}
    # Check if we have multiple symbols
    if isinstance(data.columns, pd.MultiIndex):
        # For multiple symbols
        for symbol in symbols:
            # Get data for single symbol and flatten the MultiIndex
            df_single = data.xs(symbol, level=1, axis=1)
            data_by_symbol[symbol] = df_single

    else:
        # For single symbol, ignore
        print("\nPrice data of single symbol:")
        print(data.head())
    return data_by_symbol
    

if __name__ == '__main__':
    test()