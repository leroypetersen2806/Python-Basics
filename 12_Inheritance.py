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


# Developer class is inheriting from the Employee class
# Method resolution order is when Python looks for the methods in base/parent classes
class Developer(Employee):
    """ Created Inherited class Developer """

    # Can make changes to subclasses, without breaking anything in the parent class
    # Parent class variables is accessible by the sub/child classes
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        """Setting Developers Programming Language"""
        # Both lines below calls the __init__ method of the Employee class
        # Use super() with single inheritance as it is more maintainable
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    """Managers list of Employees"""

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """Add Employee to Managers list"""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """Remove Employee from Managers list"""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


# Below instances now contains the 4th argument of the programming language
DEV_1 = Developer("Leroy", "Petersen", 50000, "Python")
DEV_2 = Developer("Test", "Employee", 60000, "Java")

MGR_1 = Manager("Sue", "Smith", 90000, [DEV_1])

# isinstance() - Tells us if an object is an instance of a class
print(isinstance(MGR_1, Manager))  # Return True
print(isinstance(MGR_1, Employee))  # Return True
print(isinstance(MGR_1, Developer))  # Return False as it only inherits Employee class

# issbuclass() - Tells us if class is a subclass of another class
print(issubclass(Developer, Employee))  # Returns True
print(issubclass(Manager, Employee))  # Returns True
print(issubclass(Manager, Developer))  # Returns False

# print(MGR_1.email)
# MGR_1.add_emp(DEV_2)
# MGR_1.remove_emp(DEV_1)
# MGR_1.print_emp()

# print(DEV_1.email)
# print(DEV_1.prog_lang)

# print(DEV_1.email)
# print(DEV_2.email)

# print(DEV_1.pay)
# DEV_1.applay_raise()
# print(DEV_1.pay)
