# Input
appliance_name = input("Enter the name of the appliance: ")
cost = float(input("Enter the cost of the appliance: "))

# Processing
warranty = 0.10 * cost if cost > 1000 else 0.05 * cost
total = cost + warranty

# Output
print(f"\nAppliance: {appliance_name}")
print(f"Cost: ${cost:.2f}")
print(f"Warranty Cost: ${warranty:.2f}")
print(f"Total Cost (including warranty): ${total:.2f}")

