# Input
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
msrp = float(input("Enter the MSRP price: "))
discount_percent = float(input("Enter the discount percent (as a decimal, e.g., 0.15 for 15%): "))

# Processing
amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

# Output
print(f"\nMake: {make}")
print(f"Model: {model}")
print(f"MSRP: ${msrp:.2f}")
print(f"Discount Percent: {discount_percent*100:.2f}%")
print(f"Amount Off: ${amount_off:.2f}")
print(f"Discounted Price: ${discounted_price:.2f}")

