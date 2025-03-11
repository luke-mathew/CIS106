def calculate_commission_and_target(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    next_year_target = sales * 0.05
    return commission, next_year_target

def main():
    salesperson_name = input("Enter salesperson's last name: ")
    sales = float(input("Enter the total sales: "))

    commission, next_year_target = calculate_commission_and_target(sales)

    print(f"Salesperson: {salesperson_name}")
    print(f"Commission: ${commission:.2f}")
    print(f"Next Year's Sales Target: ${next_year_target:.2f}")

main()

