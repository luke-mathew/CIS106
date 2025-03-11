class Employee:
    """Represents an employee with a salary and calculates a bonus based on a given rate."""
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def compute_bonus(self, rate):
        """Calculates the employee's bonus as salary * rate."""
        return self.salary * rate

    def display_info(self):
        """Displays employee details."""
        return f"Employee: {self.last_name}, {self.first_name} - Salary: ${self.salary:,.2f}"


def test_employee():
    """Tests the Employee class."""
    emp = Employee("Luke", "Mathew", 60000)
    print(emp.display_info())
    bonus_rate = float(input("Enter bonus rate (e.g., 0.10 for 10%): "))
    print(f"Bonus: ${emp.compute_bonus(bonus_rate):,.2f}")


class Student:
    """Represents a student and calculates tuition based on district code."""
    
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        """Calculates tuition based on district code."""
        rate = 250 if self.district_code == 'I' else 500
        return self.enrolled_credits * rate

    def display_info(self):
        """Displays student details and tuition owed."""
        return f"Student: {self.last_name}, {self.first_name} - Tuition Owed: ${self.compute_tuition():,.2f}"


def test_student():
    """Tests the Student class."""
    stud = Student("Luke", "Mathew", "O", 12)  # Example: Out-of-district student with 12 credits
    print(stud.display_info())


if __name__ == "__main__":
    test_employee()
    test_student()

