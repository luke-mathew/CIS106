# Input
last_name = input("Enter your last name: ")
dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: "))

# Processing
adjusted_income = gross_income - (dependents * 12000)
tax_rate = 0.20 if adjusted_income > 50000 else 0.10
income_tax = max(adjusted_income * tax_rate, 100)  # Ensures tax is at least $100

# Output
print(f"\nLast Name: {last_name}")
print(f"Gross Income: ${gross_income:.2f}")
print(f"Number of Dependents: {dependents}")
print(f"Adjusted Gross Income: ${adjusted_income:.2f}")
print(f"Income Tax: ${income_tax:.2f}")

