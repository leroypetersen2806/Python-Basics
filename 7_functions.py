'''
# Functions
- Allows re-use of code without repeating ourselves
'''
#- Defining a function
def hello_test():
    pass  # Cannot leave function blank, pass says we do not want to do anthing with it yet.

def hello_func():  # Parent
    return 'Hello Function!'  # Returns the string

def hello(greeting="Hello"):  # Has a parameter "greeting" with defaul value "Hello"
    return f"{greeting} Function."

hello_test()  # Executes the function - With only pass in function
print(hello_func)  # Return that this is a function at memory location
print(hello_test())  # Executes the function, but will return 'None'
hello_func()  # Executes the function

print(hello_func()) # Prints out the returned string from the function
print(len(hello_func()))  # Returns the length of the returned string
print(hello_func().upper())  # Returned string in uppercase
print(hello("Hi"))  # Passing "Hi" set greeting variable equal to "Hi" - If blank, will use default "Hello"

'''
#- *args and **kwargs
- Allows us to accept an arbitrary number of positional or keyword arguments
- if student_info function takes positional arguments that represents the classes that the student takes
- keyword passed in will be random information about the student
- does not have to be *args, **kwargs, but it is a convention used. can be *pietie, **sana
'''
def student_info(*args, **kwargs):
    print(args)  #- Returns tuple with all our positional arguments
    print(kwargs)  #- Returns dictionary with all our keywords and values.

student_info('Math', 'Art', name='John', age=25)  # Positional arguments (Math, Art), keyword arguments(name='John', age=25)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(courses, info)  # Passes in the complete list and dictionary as a position arguments
student_info(*courses, **info)  # Passes in the list as position arg and info as the keyword args

'''
# Examples
'''
#- Number of days per month. First index is a place holder, not being used.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    # Returns Truee for leap years, False for non-leap years.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    # Return number of days in that month in that year
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))  # Returns false
print(is_leap(2020))  # Returns True for leap years

print(days_in_month(2017, 2))  # This will return 28 days
print(days_in_month(2020, 2))  # Returns 29 days
