# Initialize counters
total_gross_pay = 0
count_employees = 0

# Prompt user to continue
continue_program = input("Do you want to enter employee data? (Yes/No): ")

while continue_program.lower() == "yes":
    # Input
    last_name = input("Enter employee last name: ")
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    # Processing
    if hours_worked > 40:
        gross_pay = (40 * hourly_rate) + ((hours_worked - 40) * hourly_rate * 1.5)
    else:
        gross_pay = hours_worked * hourly_rate

    total_gross_pay += gross_pay
    count_employees += 1

    # Output
    print(f"\nEmployee: {last_name}")
    print(f"Gross Pay: ${gross_pay:.2f}")

    # Ask user if they want to continue
    continue_program = input("\nDo you want to enter another employee? (Yes/No): ")

# Display summary
if count_employees > 0:
    average_pay = total_gross_pay / count_employees
else:
    average_pay = 0

print(f"\nTotal Gross Pay: ${total_gross_pay:.2f}")
print(f"Number of Employees: {count_employees}")
print(f"Average Pay: ${average_pay:.2f}")

