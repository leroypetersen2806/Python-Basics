# Python Object-Oriented Programming

"""
Allow us to logical group data and functions in order
to re-use and easy to build upon.
Creating a blueprint for employee

Instance vars contain data that is UNIQUE to each instance.
"""

# Class is a blueprint for creating instance
class Employee:
    # Initialise // Constructor method (self is the instance. e.g. emp_1.first = "Meh")
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    # Method also automatically take the instance (emp_1 / emp_2) as the first argument (self)
    def fullname(self):
        return f"{self.first} {self.last}"


"""
# emp_1 and emp_2 are there own unique instances of the class employee
emp_1 = Employee()
emp_2 = Employee()

# Instance variables
Don't get much benefit from classes if done as per below.

emp_1.first = "Leroy"
emp_1.last = "Petersen"
emp_1.email = f"{emp_1.first}.{emp_1.last}@company.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = f"{emp_1.first}.{emp_1.last}@company.com"
emp_2.pay = 50000
"""


emp_1 = Employee("Leroy", "Petersen", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

# Similar, but not exactly the same
print(Employee.fullname(emp_1))
print(emp_1.fullname())

