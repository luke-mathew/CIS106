# Input
ticker = input("Enter the stock ticker symbol: ")
shares = int(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

# Processing
amount_invested = shares * cost_per_share

# Output
print(f"\nStock: {ticker}")
print(f"Amount Invested: ${amount_invested:.2f}")

