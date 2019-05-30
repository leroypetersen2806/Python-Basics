# Property decorator - Allows define method but access it as an attribute
class Employee:
    """Create a new employee"""

    def __init__(self, first, last):
        self.first = first

        self.last = last
        # self.email = f"{first}.{last}@company.com"

    # @property decorator allows us not to use EMP_1.email(), but instead EMP_1.email - See below
    @property
    def fullname(self):
        """Returns the fullname of the employee"""
        return f"{self.first} {self.last}"
        # return "{} {}".format(self.first, self.last)

    # Decorator allows us to update an instance variable
    # Used with the original function name adding .setter at the end
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    @property
    def email(self):
        """Returns email of Employee"""
        return f"{self.first}.{self.last}@email.com"


EMP_1 = Employee("John", "Smith")
EMP_1.first = "Jim"

EMP_1.fullname = "Leroy Petersen"

print(EMP_1.first)

# @property decorator allows us not to use EMP_1.email(), but instead EMP_1.email
print(EMP_1.email)
print(EMP_1.fullname)

del EMP_1.fullname
