import datetime


class Employee:
    """Creating a class Employee"""

    num_of_emps = 0
    raise_amount = 1.04  # raise_amount is a class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        # Not using self as want it globally assigned instead of per instance (Which makes sense right, right)
        # Automatically increments when the instances are created (Returns the instances for the class)
        Employee.num_of_emps += 1

    def fullname(self):
        """Returns Employee Instance full name"""
        return f"{self.first} {self.last}"

    def applay_raise(self):
        """Applies a raise to employee"""
        # Have to add self.raise amount as you have to access it via the instance
        self.pay = int(self.pay * self.raise_amount)

    # Takes in the class as the first argument and no longer the instance.
    @classmethod  # This is a decorator
    def set_raise_amount(cls, amount):
        """Using a class method"""
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """Constructor that splits the string"""
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # Static methods dont pass anything automatically. Acts like regular methods
    # Dont access the instance or the class in the method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


EMP_1 = Employee("Leroy", "Petersen", 50000)
EMP_2 = Employee("Test", "User", 60000)

# Automatically accepts the class, so no need to add it.
Employee.set_raise_amount(1.05)

# Use class methods as alternative constructors
# EMP_STR_1 = "John-Doe-70000"
# EMP_STR_2 = "Steve-Smit-30000"
# EMP_STR_3 = "Jane-Doe-90000"

# NEW_EMP_1 = Employee.from_string(EMP_STR_1)

# print(NEW_EMP_1.email)
# print(NEW_EMP_1.pay)


MY_DATE = datetime.date(2016, 7, 11)
print(Employee.is_workday(MY_DATE))
