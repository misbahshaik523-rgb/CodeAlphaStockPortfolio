# CodeAlpha Task 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "AMZN": 190,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available in our list.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid number.")

print("\n===== Portfolio Summary =====")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value

    print(
        f"{stock}: {quantity} shares × "
        f"${stock_prices[stock]} = ${value}"
    )

print(f"\nTotal Investment Value: ${total_investment}")
