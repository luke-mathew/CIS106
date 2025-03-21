# Base Employee class
class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    
    def long_term_bonus(self):
        return self.salary * 0.40
    
    def __str__(self):
        return f"{self.first} {self.last} - Salary: ${self.salary}"

# Derived Manager class
class Manager(Employee):
    pass  # Inherits long_term_bonus as 40% of salary

# Derived Executive class
class Executive(Employee):
    def long_term_bonus(self):
        return self.salary * 0.50  # Overridden method
    
    def executive_bonus(self):
        return self.salary * 2.00

# Instantiate and test
m = Manager("John", "Doe", 100000)
e = Executive("Jane", "Smith", 150000)

print(m)
print("Manager Long Term Bonus:", m.long_term_bonus())
print(e)
print("Executive Long Term Bonus:", e.long_term_bonus())
print("Executive Bonus:", e.executive_bonus())

# Base Car class
class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price
        self.discount_price = sticker_price * 0.90
    
    def __str__(self):
        return f"{self.make} {self.model} - Sticker Price: ${self.sticker_price}, Discount Price: ${self.discount_price}"

# Derived Sport class
class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = 0
        self.sport_engine = 0
        self.sport_interior = 0
    
    def add_sport_wheels(self, option):
        if option == "Y":
            self.sport_wheels = 1000
    
    def add_sport_engine(self, option):
        if option == "Y":
            self.sport_engine = 3000
    
    def add_sport_interior(self, option):
        if option == "Y":
            self.sport_interior = 2000
    
    def price_with_options(self):
        return self.discount_price + self.sport_wheels + self.sport_engine + self.sport_interior

# Derived Luxury class
class Luxury(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.gps = 0
        self.self_driving = 0
    
    def add_gps(self, option):
        if option == "Y":
            self.gps = 5000
    
    def add_self_driving(self, option):
        if option == "Y":
            self.self_driving = 10000
    
    def price_with_options(self):
        return self.discount_price + self.gps + self.self_driving

# Instantiate and test Sport car
s_car = Sport("Ford", "Mustang", 50000)
s_car.add_sport_wheels("Y")
s_car.add_sport_engine("Y")
s_car.add_sport_interior("Y")
print(s_car)
print("Sport Car Price with Options:", s_car.price_with_options())

# Instantiate and test Luxury car
l_car = Luxury("Tesla", "Model S", 80000)
l_car.add_gps("Y")
l_car.add_self_driving("Y")
print(l_car)
print("Luxury Car Price with Options:", l_car.price_with_options())

