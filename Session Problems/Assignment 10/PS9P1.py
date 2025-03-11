def calculate_total(quantity, price):
    total = quantity * price
    if total > 10000:
        total *= 0.90  # Apply 10% discount if total is greater than $10,000
    return total

def main():
    extended_price_total = 0
    while True:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        
        total = calculate_total(quantity, price)
        extended_price_total += total
        
        print(f"Quantity: {quantity}, Price: ${price:.2f}, Total: ${total:.2f}")
        
        continue_program = input("Do you want to continue? (Yes or No): ")
        if continue_program.lower() != "yes":
            break
    
    print(f"\nTotal of all extended prices: ${extended_price_total:.2f}")

main()

