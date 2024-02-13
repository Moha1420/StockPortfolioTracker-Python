import requests
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Registered users (will store usernames)
registered_users = set()

# Function to authenticate user credentials
def authenticate(username, password):
    # Check if username and password match any registered user
    # You can implement your authentication logic here
    return username in registered_users and password == "password123"  # Dummy authentication for demonstration

# Function to handle user registration
def register():
    username = entry_username.get()
    password = entry_password.get()
    if username.isalpha() and password.isdigit():
        if username not in registered_users:
            registered_users.add(username)
            messagebox.showinfo("Registration", "Registration successful.")
            # Automatically log in after registration
            logged_in_user = username
            show_portfolio_ui()
        else:
            messagebox.showerror("Registration Failed", "Username already exists.")
    else:
        messagebox.showerror("Registration Failed", "Invalid username or password. Username should be text only and password should be number only.")

# Function to handle user login
def login():
    global logged_in_user
    username = entry_username.get()
    password = entry_password.get()
    if username in registered_users:
        if authenticate(username, password):
            logged_in_user = username
            messagebox.showinfo("Login", f"Welcome, {username}!")
            show_portfolio_ui()
        else:
            messagebox.showerror("Login Failed", "Invalid password.")
    else:
        messagebox.showerror("Login Failed", "You need to register first.")

# Function to handle logout
def logout():
    global logged_in_user
    logged_in_user = None
    show_login_ui()

# Function to display portfolio UI after successful login
def show_portfolio_ui():
    login_frame.pack_forget()
    portfolio_frame.pack()

# Function to display login UI
def show_login_ui():
    portfolio_frame.pack_forget()
    login_frame.pack()

# Function to display stock adding UI
def show_add_stock_ui():
    portfolio_frame.pack_forget()
    add_stock_frame.pack()

# Function to display stock removing UI
def show_remove_stock_ui():
    portfolio_frame.pack_forget()
    remove_stock_frame.pack()

# Function to display stock tracking UI
def show_stock_tracking_ui():
    portfolio_frame.pack_forget()
    stock_tracking_frame.pack()

# Function to get real-time stock data
def get_stock_data(symbol):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key from Alphavantage
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['Global Quote']

# Function to add a stock to the portfolio
def add_stock():
    symbol = entry_symbol.get().upper()
    stock_data = get_stock_data(symbol)
    if stock_data:
        portfolio[symbol] = stock_data
        messagebox.showinfo("Success", f"{symbol} added to portfolio.")
    else:
        messagebox.showerror("Error", f"Failed to add {symbol} to portfolio. Please check the symbol.")

# Function to remove a stock from the portfolio
def remove_stock():
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

# Main program loop to Display UI using Python Tkinter 
def main():
    global entry_symbol, entry_username, entry_password, login_frame, portfolio_frame, portfolio, logged_in_user
    
    root = tk.Tk()
    root.title("Stock Portfolio Tracker")

    # Frames for login and portfolio UI
    login_frame = tk.Frame(root, bg="#4CAF50")  # Set background color to match the stock tracker symbol
    portfolio_frame = tk.Frame(root)
    add_stock_frame = tk.Frame(root)
    remove_stock_frame = tk.Frame(root)
    stock_tracking_frame = tk.Frame(root)

    # Login UI
    label_username = tk.Label(login_frame, text="Username:", bg="#4CAF50")  # Set background color
    label_username.grid(row=0, column=0, padx=5, pady=5)
    entry_username = tk.Entry(login_frame)
    entry_username.grid(row=0, column=1, padx=5, pady=5)

    label_password = tk.Label(login_frame, text="Password:", bg="#4CAF50")  # Set background color
    label_password.grid(row=1, column=0, padx=5, pady=5)
    entry_password = tk.Entry(login_frame, show="*")
    entry_password.grid(row=1, column=1, padx=5, pady=5)

    button_login = tk.Button(login_frame, text="Login", command=login, bg="#4CAF50", fg="white")  # Set background color and foreground color
    button_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    button_register = tk.Button(login_frame, text="Register", command=register, bg="#4CAF50", fg="white")  # Set background color and foreground color
    button_register.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Portfolio UI
    label_symbol = tk.Label(portfolio_frame, text="Enter Stock Symbol:")
    label_symbol.pack()

    entry_symbol = tk.Entry(portfolio_frame, font=('Arial', 16, 'bold'), width=30)
    entry_symbol.pack(pady=10, padx=20)

    button_add = tk.Button(portfolio_frame, text="Add Stock", command=add_stock, bg="#4CAF50", fg="white", width=30, height=5, font=('Arial', 12, 'bold'))
    button_add.pack(pady=10)

    button_remove = tk.Button(portfolio_frame, text="Remove Stock", command=remove_stock, bg="#f44336", fg="white", width=30, height=5, font=('Arial', 12, 'bold'))
    button_remove.pack(pady=10)

    button_display = tk.Button(portfolio_frame, text="Display Portfolio", command=display_portfolio, bg="#2196F3", fg="white", width=30, height=5, font=('Arial', 12, 'bold'))
    button_display.pack(pady=10)

    button_logout = tk.Button(portfolio_frame, text="Logout", command=logout, bg="gray", fg="white", width=5, height=1, font=('Arial', 10, 'bold'))
    button_logout.pack(pady=10)

    # Initial setup
    logged_in_user = None
    portfolio = {}
    show_login_ui()

    root.mainloop()

if __name__ == "__main__":
    main()
