
# Input
last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary: "))
job_level = int(input("Enter job level: "))

# Processing
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus = salary * bonus_rate

# Output
print(f"\nEmployee Last Name: {last_name}")
print(f"Bonus Amount: ${bonus:.2f}")
