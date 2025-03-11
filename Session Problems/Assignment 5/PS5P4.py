# Input
tickets = int(input("Enter the number of concert tickets: "))

# Processing
if tickets >= 25:
    price_per_ticket = 50
elif tickets >= 10:
    price_per_ticket = 60
elif tickets >= 5:
    price_per_ticket = 70
else:
    price_per_ticket = 75

total_cost = tickets * price_per_ticket

# Output
print(f"\nNumber of Tickets: {tickets}")
print(f"Price Per Ticket: ${price_per_ticket:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

