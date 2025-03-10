# Input
last_name = input("Enter your last name: ")
midterm = float(input("Enter your midterm score: "))
final = float(input("Enter your final exam score: "))

# Processing
total_score = midterm + final

# Output
print(f"\nStudent: {last_name}")
print(f"Total Exam Points: {total_score:.2f}")

