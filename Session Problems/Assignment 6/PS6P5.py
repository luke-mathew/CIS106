# Initialize total discount
total_discount = 0

# Prompt user to continue
continue_program = input("Do you want to enter an order? (Yes/No): ")

while continue_program.lower() == "yes":
    # Input
    quantity = int(input("Enter quantity: "))
    price_per_item = float(input("Enter price per item: "))

    # Processing
    extended_price = quantity * price_per_item
    if extended_price > 10000:
        discount_rate = 0.25
    else:
        discount_rate = 0.10

    discount_amount = extended_price * discount_rate
    total_price = extended_price - discount_amount
    total_discount += discount_amount

    # Output
    print(f"\nExtended Price: ${extended_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total Price: ${total_price:.2f}")

    # Ask user if they want to continue
    continue_program = input("\nDo you want to enter another order? (Yes/No): ")

# Display total discount amount
print(f"\nTotal Discount Given: ${total_discount:.2f}")

