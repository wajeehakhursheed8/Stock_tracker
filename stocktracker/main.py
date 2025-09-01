
import pandas as pd #cvs files k liye dataframe

print('WELCOME TO STOCK INFO!')

stocks= {
    # Technology
    "AAPL": {"price": 178.5, "quantity": 10},    # Apple
    "MSFT": {"price": 329.8, "quantity": 5},     # Microsoft
    "TSLA": {"price": 244.3, "quantity": 8},     # Tesla
    "GOOGL": {"price": 132.7, "quantity": 12},   # Alphabet
    "AMZN": {"price": 138.5, "quantity": 7},     # Amazon
    "NVDA": {"price": 452.2, "quantity": 4},     # NVIDIA
    "META": {"price": 298.1, "quantity": 6},     # Meta Platforms

    # Banking & Finance
    "JPM": {"price": 145.9, "quantity": 9},      # JPMorgan Chase
    "BAC": {"price": 28.4, "quantity": 20},      # Bank of America
    "GS": {"price": 345.2, "quantity": 3},       # Goldman Sachs

    # Energy
    "XOM": {"price": 108.7, "quantity": 15},     # ExxonMobil
    "CVX": {"price": 164.1, "quantity": 7},      # Chevron
    "BP": {"price": 36.9, "quantity": 18},       # BP plc

    # Pharmaceuticals / Healthcare
    "PFE": {"price": 38.2, "quantity": 20},      # Pfizer
    "JNJ": {"price": 165.3, "quantity": 6},      # Johnson & Johnson
    "MRK": {"price": 110.6, "quantity": 8},      # Merck & Co.

    # Consumer Goods
    "KO": {"price": 60.7, "quantity": 14},       # Coca-Cola
    "PEP": {"price": 181.5, "quantity": 5},      # PepsiCo
    "NKE": {"price": 109.4, "quantity": 9},      # Nike
    "MCD": {"price": 287.3, "quantity": 4}       # McDonald’s
}


def get_price(stockname):
    if stockname in stocks:
        return stocks[stockname]["price"]
    else:
        return None
    

def total(stocks):
        total_invest=0
        for stock in stocks:
            price=stocks[stock]['price']
            quantity=stocks[stock]['quantity']
            total_invest+= price*quantity
        return total_invest
        
results = []  # to store user inputs and calculated values
   

while True:
    stockname1 = input("Enter the stock name (or 'done'): ").upper()
    if stockname1 == 'DONE':
        break
    
    if stockname1 not in stocks:
        print("Error 404: Stock not found!")
        continue #ye continue restart krdega loop ko 

    stockname2 = input("Enter the quantity: ")
    try:
        quantity = int(stockname2)
    except ValueError:
        print("Invalid quantity! Please enter a number.")
        continue
    
    price = get_price(stockname1)
    total_value = price * quantity
    print(f"The price of {stockname1} is ${price}")
    print(f"Total value for {quantity} shares: ${total_value}")


    results.append({
    "Stock": stockname1,
    "Quantity": quantity,
    "Price": price,
    "Total Value": total_value
    })

    
opinion=['yes','no']
user=input('Do you want to calculate the total investment of stocks?\n(Yes/No)').lower()
if user == opinion[1]:
    print("Alright!\n Let me know if you want more info about stocks!!")
else:
    print(f"The total investment of your stock is: ${total(stocks)}")
     
# Ask the user if they want to save the results
save_csv = input("Do you want to save the results to a CSV file? (Yes/No): ").lower()

if save_csv == 'yes':
    import pandas as pd
    df = pd.DataFrame(results)  # convert list of dictionaries to DataFrame
    df.to_csv("stock_results.csv", index=False)
    print("All your stock info has been saved to 'stock_results.csv'.")
else:
    print("Okay! The results were not saved. Exiting program.")

        



           

    
    






    
