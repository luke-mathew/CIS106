# Input
item = input("Enter the item (A or other): ")
quantity = int(input("Enter the quantity: "))

# Processing
unit_price = 10.00 if item == "A" else 20.00
extended_price = quantity * unit_price

# Output
print(f"\nItem: {item}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")

