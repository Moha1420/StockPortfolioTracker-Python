import requests
import pandas as pd
import tkinter as tk
from tkinter import messagebox

def get_stock_data(symbol):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key from Alphavantage
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['Global Quote']

# the function get_stock_data(symbol) fetches real-time stock data using the Alpha Vantage API. The symbol parameter represents the stock symbol or ticker symbol of a publicly traded company.

# Stock symbols or ticker symbols are typically composed of a combination of letters and sometimes numbers, and they represent a particular publicly traded company on a stock exchange. For example:

# Apple Inc.: AAPL
# Microsoft Corporation: MSFT
# Amazon.com Inc.: AMZN
def add_stock():
    symbol = entry_symbol.get().upper()
    stock_data = get_stock_data(symbol)
    if stock_data:
        portfolio[symbol] = stock_data
        messagebox.showinfo("Success", f"{symbol} added to portfolio.")
    else:
        messagebox.showerror("Error", f"Failed to add {symbol} to portfolio. Please check the symbol.")

def remove_stock():
    symbol = entry_symbol.get().upper()
    if symbol in portfolio:
        del portfolio[symbol]
        messagebox.showinfo("Success", f"{symbol} removed from portfolio.")
    else:
        messagebox.showerror("Error", f"{symbol} is not in the portfolio.")

def display_portfolio():
    if portfolio:
        df = pd.DataFrame.from_dict(portfolio, orient='index')
        messagebox.showinfo("Portfolio", df.to_string())
    else:
        messagebox.showinfo("Portfolio", "Portfolio is empty.")

def main():
    global entry_symbol, portfolio
    portfolio = {}
    
    root = tk.Tk()
    root.title("Stock Portfolio Tracker")
    root.configure(bg="gray")

    label_symbol = tk.Label(root, text="Enter Stock Symbol:", bg="gray")
    label_symbol.pack()

    entry_symbol_var = tk.StringVar()
    entry_symbol = tk.Entry(root, textvariable=entry_symbol_var, font=('Arial', 16, 'bold'), width=30)
    entry_symbol.pack(pady=10, padx=20)

    button_add = tk.Button(root, text="Add Stock", command=add_stock, bg="#4CAF50", fg="white", width=30, height=5, font=('Arial', 12, 'bold'))
    button_add.pack(pady=10)

    button_remove = tk.Button(root, text="Remove Stock", command=remove_stock, bg="#f44336", fg="white", width=30, height=5, font=('Arial', 12, 'bold'))
    button_remove.pack(pady=10)

    button_display = tk.Button(root, text="Display Portfolio", command=display_portfolio, bg="#2196F3", fg="white", width=30, height=5, font=('Arial', 12, 'bold'))
    button_display.pack(pady=10)

    button_exit = tk.Button(root, text="Exit", command=root.destroy, bg="gray", fg="white", width=5, height=1, font=('Arial', 10, 'bold'))
    button_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
