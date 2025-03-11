# Input
books = int(input("Enter the number of books: "))
cost_per_book = float(input("Enter the cost per book: "))

# Processing
order_total = books * cost_per_book
shipping = 0 if order_total > 50 else 25

# Output
print(f"\nOrder Total: ${order_total:.2f}")
print(f"Shipping Charge: ${shipping:.2f}")

