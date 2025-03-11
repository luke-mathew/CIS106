def determine_pay_rate(job_code):
    if job_code == "L":
        return 25
    elif job_code == "A":
        return 30
    elif job_code == "J":
        return 50
    return 0  # Default case if job code is invalid

def main():
    total_gross_pay = 0
    while True:
        last_name = input("Enter employee's last name: ")
        job_code = input("Enter job code (L, A, J): ")
        hours_worked = float(input("Enter hours worked: "))
        
        pay_rate = determine_pay_rate(job_code)
        if hours_worked > 40:
            gross_pay = (40 * pay_rate) + ((hours_worked - 40) * pay_rate * 1.5)
        else:
            gross_pay = hours_worked * pay_rate
        
        total_gross_pay += gross_pay
        print(f"{last_name}: Gross Pay: ${gross_pay:.2f}")
        
        continue_program = input("Do you want to continue? (Yes or No): ")
        if continue_program.lower() != "yes":
            break
    
    print(f"\nTotal of all gross pay: ${total_gross_pay:.2f}")

main()

