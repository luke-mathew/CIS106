# Global variables
total = 0
tax = 0

def calculate_total_and_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = total * 0.07

def main():
    quantity = int(input("Enter quantity of the item: "))
    unit_price = float(input("Enter unit price of the item: "))

    calculate_total_and_tax(quantity, unit_price)

    print(f"Total Price: ${total:.2f}")
    print(f"Tax: ${tax:.2f}")

main()

