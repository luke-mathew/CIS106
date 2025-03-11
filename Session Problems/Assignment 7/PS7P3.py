
def employee_bonus():
    total_bonus = 0
    with open("employees.txt", "r") as file:
        lines = file.readlines()

    for i in range(0, len(lines), 2):  # Every two lines, one for name, one for salary
        last_name = lines[i].strip()
        salary = float(lines[i + 1].strip())
        
        if salary >= 100000:
            bonus_rate = 0.20
        elif salary >= 50000:
            bonus_rate = 0.15
        else:
            bonus_rate = 0.10
        
        bonus = salary * bonus_rate
        total_bonus += bonus
        
        print(f"{last_name}: Salary = ${salary:,.2f}, Bonus = ${bonus:,.2f}")
    
    print(f"\nTotal Bonuses Paid: ${total_bonus:,.2f}")

employee_bonus()

