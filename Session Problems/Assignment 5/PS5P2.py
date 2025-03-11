# Input
part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))

# Processing
if part_number in ["10", "55"]:
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number in ["80", "70"]:
    unit_cost = 3.00
else:
    unit_cost = 5.00

total_cost = quantity * unit_cost

# Output
print(f"\nPart Number: {part_number}")
print(f"Unit Cost: ${unit_cost:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

