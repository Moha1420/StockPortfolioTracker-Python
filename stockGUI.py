import requests
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Function to get real-time stock data
def get_stock_data(symbol):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key from Alpha Vantage
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['Global Quote']

# Function to add a stock to the portfolio
def add_stock():
    global entry_symbol
    symbol = entry_symbol.get().upper()
    stock_data = get_stock_data(symbol)
    if stock_data:
        portfolio[symbol] = stock_data
        messagebox.showinfo("Success", f"{symbol} added to portfolio.")
    else:
        messagebox.showerror("Error", f"Failed to add {symbol} to portfolio. Please check the symbol.")

# Function to remove a stock from the portfolio
def remove_stock():
    global entry_symbol
    symbol = entry_symbol.get().upper()
    if symbol in portfolio:
        del portfolio[symbol]
        messagebox.showinfo("Success", f"{symbol} removed from portfolio.")
    else:
        messagebox.showerror("Error", f"{symbol} is not in the portfolio.")

# Function to display the portfolio
def display_portfolio():
    if portfolio:
        df = pd.DataFrame.from_dict(portfolio, orient='index')
        messagebox.showinfo("Portfolio", df.to_string())
    else:
        messagebox.showinfo("Portfolio", "Portfolio is empty.")

# Main program loop
def main():
    global entry_symbol
    root = tk.Tk()
    root.title("Stock Portfolio Tracker")

    label_symbol = tk.Label(root, text="Enter Stock Symbol:")
    label_symbol.pack()

    entry_symbol = tk.Entry(root)
    entry_symbol.pack()

    button_add = tk.Button(root, text="Add Stock", command=add_stock, bg="#4CAF50", fg="white", padx=10, pady=5)
    button_add.pack()

    button_remove = tk.Button(root, text="Remove Stock", command=remove_stock, bg="#f44336", fg="white", padx=10, pady=5)
    button_remove.pack()

    button_display = tk.Button(root, text="Display Portfolio", command=display_portfolio, bg="#2196F3", fg="white", padx=10, pady=5)
    button_display.pack()

    button_exit = tk.Button(root, text="Exit", command=root.destroy, bg="gray", fg="white", padx=10, pady=5)
    button_exit.pack()

    root.mainloop()

if __name__ == "__main__":
    portfolio = {}
    main()
