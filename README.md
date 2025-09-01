# Stock_tracker
#  Stock Info (Python)

A simple Python program that allows users to view stock prices, calculate investments, and save results into a CSV file. The project simulates a stock portfolio by providing predefined stock data from multiple sectors (technology, banking, energy, healthcare, consumer goods).

---

 Features
- Predefined stock data with prices and quantities  
- Search for a stock by its ticker symbol (e.g., `AAPL`, `TSLA`)  
- Enter your desired quantity to calculate investment value  
- Option to calculate the **total portfolio investment**  
- Save your results into a **CSV file** for later use  
- Handles invalid inputs gracefully (e.g., wrong ticker or non-numeric quantities)  

---

  Requirements
- Python 3.x  
- [pandas](https://pandas.pydata.org/) library (only required if you want to save results to CSV)

Install pandas with:
```bash
pip install pandas
```

How to Use:
Enter the stock symbol (e.g., AAPL, MSFT, TSLA).
Enter the quantity of shares.
The program will show the price and total value of your input.
Repeat until you type done.
Choose whether to:
Calculate the total portfolio investment
Save results to a CSV file

Future Improvements:
Fetch real-time stock prices from an API
Add more stock sectors and tickers
GUI version for easier interaction

