# Input
principal = float(input("Enter the principal amount: "))
years = int(input("Enter the years to maturity: "))

# Processing
if principal > 100000 and years == 5:
    interest_rate = 0.06
elif 50000 <= principal <= 100000 and years == 10:
    interest_rate = 0.05
elif 50000 <= principal <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

interest = principal * interest_rate

# Output
print(f"\nPrincipal Amount: ${principal:.2f}")
print(f"Interest Rate: {interest_rate * 100:.2f}%")
print(f"First Year Interest: ${interest:.2f}")

