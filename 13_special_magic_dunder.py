# Magic Methods - Helps Emulates special bahaviour in Python
# Also allow us to use operator overloading


class Employee:
    """Creates and Employee"""

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay

    def fullname(self):
        """Returns Employee fullname"""
        return f"{self.first} {self.last}"

    def apply_raise(self):
        """Apply Employee raise"""
        self.pay = int(self.pay * self.raise_amount)

    # Used for debugging and logging
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    # Readable representation of the object - Used as display to end user
    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    # Overloading dunder add
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


EMP_1 = Employee("Leroy", "Petersen", 50000)
EMP_2 = Employee("Test", "Employee", 60000)

print(EMP_1 + EMP_2)


print(len("test"))
print("test".__len__())

# Uses overloaded dundar __len__
print(len(EMP_1))

# print(EMP_1)

# print(repr(EMP_1))
# print(str(EMP_1))
# print(EMP_1.__repr__())
# print(EMP_1.__str__())

# Dunder Add
# print(int.__add__(1, 2))  # Adds the two values and return result


# Read up on documentation for Emulating numeric Types https://docs.python.org
