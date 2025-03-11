def calculate_extended_price():
    total_price = 0
    order_count = 0
    with open("orders.txt", "r") as file:
        lines = file.readlines()

    for i in range(0, len(lines), 3):  # Every three lines: item, quantity, price
        item_name = lines[i].strip()
        quantity = int(lines[i + 1].strip())
        price = float(lines[i + 2].strip())
        
        extended_price = quantity * price
        total_price += extended_price
        order_count += 1
        
        print(f"Item: {item_name}, Quantity: {quantity}, Price: ${price:,.2f}, Extended Price: ${extended_price:,.2f}")
    
    average_order = total_price / order_count if order_count != 0 else 0
    print(f"\nTotal Extended Price: ${total_price:,.2f}")
    print(f"Number of Orders: {order_count}")
    print(f"Average Order: ${average_order:,.2f}")

calculate_extended_price()

