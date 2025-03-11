def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate
    discounted_price = price - discount_amount
    return discount_amount, discounted_price

def main():
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price of one item: "))
    discount_rate = float(input("Enter the discount rate (as a decimal): "))

    discount_amount, discounted_price = calculate_discount(price, discount_rate)
    total_price = quantity * discounted_price

    print(f"Quantity: {quantity}")
    print(f"Price: ${price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")
    print(f"Total after discount: ${total_price:.2f}")

main()

