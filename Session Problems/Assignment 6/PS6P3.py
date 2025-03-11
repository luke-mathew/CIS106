# Initialize count
count_students = 0

# Prompt user to continue
continue_program = input("Do you want to enter student data? (Yes/No): ")

while continue_program.lower() == "yes":
    # Input
    last_name = input("Enter student's last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))

    # Processing
    average = (exam1 + exam2) / 2
    count_students += 1

    # Output
    print(f"\nStudent: {last_name}")
    print(f"Average Exam Score: {average:.2f}")

    # Ask user if they want to continue
    continue_program = input("\nDo you want to enter another student? (Yes/No): ")

# Display total number of students
print(f"\nTotal number of students entered: {count_students}")

