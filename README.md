
# StockPortfolioTracker-Python 
The offered code uses Tkinter in Python to create a simple GUI-driven stock portfolio tracker. This is an explanation:

Usability:

Real-time stock data is accessed by the get_stock_data(symbol) function via the Alpha Vantage API. After receiving a stock symbol, it fetches the relevant information.
The addition, deletion, and presentation of stocks in the portfolio are handled by the functions add_stock(), remove_stock(), and display_portfolio(). They use get_stock_data() to get stock data and interact with GUI elements.
Configuring the Interface:

The Tkinter GUI window is configured by the main() function. It includes buttons, labels, and entry fields for adding, removing, and displaying stocks in the portfolio.
Guide to Usage:

Users fill in the designated entry box with a stock symbol.
To add the entered stock symbol to the portfolio, they click "Add Stock".
"Remove Stock" makes it easier to get rid of .

