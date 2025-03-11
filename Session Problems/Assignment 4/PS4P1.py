# Input
quantity = int(input("Enter the quantity of the item: "))

# Processing
unit_price = 3.00 if quantity >= 1000 else 5.00
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

# Output
print(f"\nQuantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")

