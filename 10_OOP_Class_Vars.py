# Class Variable
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


EMP_1 = Employee("Leroy", "Petersen", 50000)
EMP_2 = Employee("Test", "User", 60000)

# Printing out the namespace of emp_1 (Deos not contain the raise_amount)
# Output({'first': 'Leroy', 'last': 'Petersen', 'pay': 50000, 'email': 'Leroy.Petersen@company.com'})
print(EMP_1.__dict__)

# Printing out namespace of Employee class (Does containt the raise_amount variable)
# Output({'__module__': '__main__', '__doc__': 'Creating a class Employee', 'raise_amount': 1.04,
#  '__init__': <function Employee.__init__ at 0x0000017BEAFACEA0>, 'fullname': <function Employee.fullname at 0x0000017BEAFACF28>,
#  'applay_raise': <function Employee.applay_raise at 0x0000017BEAFB8048>, '__dict__': <attribute '__dict__' of 'Employee' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Employee' objects>}
# )
print(Employee.__dict__)

# Setting raise_amount for the class to 1.05
# This sets the raise_amount for the class and the instances
Employee.raise_amount = 1.05

# Setting raise_amount for the EMP_1 to 1.06
# This will only set the raise amount for EMP_1
EMP_1.raise_amount = 1.06

# Now EMP_1 will have the raise_amount within its namespace
print(EMP_1.__dict__)

# Can access class variable (raise_amount) from both class(Employee) and instances(emp_1, emp_2)
# print(Employee.raise_amount)
print(Employee.raise_amount)
print(EMP_1.raise_amount)
print(EMP_2.raise_amount)

# print(EMP_1.pay)
# EMP_1.applay_raise()
# print(EMP_1.pay)

# Printing number of employees
print(Employee.num_of_emps)
