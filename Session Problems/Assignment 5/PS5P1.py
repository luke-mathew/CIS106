# Input
quantity = int(input("Enter the quantity of widgets: "))

# Processing
if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:
    price = 30

extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

# Output
print(f"\nQuantity: {quantity}")
print(f"Unit Price: ${price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Cost: ${total:.2f}")

