
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 120,
    "MSFT": 310
}

portfolio = {}

print("Stock Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish.\n")

while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("Invalid stock symbol. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("Invalid quantity. Enter a number.\n")
        continue

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print(f"Added {quantity} shares of {stock}.\n")

print("\nFinal Investment Report:")
total_investment = 0

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    total = price * qty
    total_investment += total
    print(f"{stock} - Quantity: {qty}, Price: {price} → {price} x {qty} = {total}")

print(f"\nTotal Investment: {total_investment}")

save = input("\nDo you want to save this report to a file? (yes/no): ").lower()
if save == 'yes':
    with open("stock_report.txt", "w") as file:
        file.write("Stock Investment Report\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            total = price * qty
