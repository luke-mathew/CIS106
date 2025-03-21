class Employee:
    def __init__(self, first, last, salary, bonus_rate):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        self.bonus_rate = bonus_rate  # New attribute for bonus rate

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def compute_bonus(self):
        return self.salary * self.bonus_rate  # Computes bonus amount

# Instantiate and test
emp1 = Employee("John", "Doe", 60000, 0.10)  # 10% bonus rate

print(f"Employee: {emp1.full_name()}")
print(f"Email: {emp1.email}")
print(f"Salary: ${emp1.salary}")
print(f"Bonus Amount: ${emp1.compute_bonus()}")

