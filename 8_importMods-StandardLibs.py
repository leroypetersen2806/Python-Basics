'''
# Importing Modules

import my_module
courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')  # When imported using 'import my_module'
print(index)
'''

'''
import my_module as mm  # Imports the module as mm and can be used to call functions

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')  # When imported using 'import my_module as mm'
print(index)
'''

'''
#- Importing the function only - Only give access to this function and no other functions
from my_module import find_index, test  # Adding ,test gives access to the test var as well.

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')  # When imported using 'from my_module import find_index
print(index)
print(test)  # prints out the value for test
'''

'''
# Import Everything - Never use this and fround upon
from my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')  # When imported using 'from my_module import find_index
print(index)
'''

'''
# Location for finding imported Modules
import sys
sys.path.append('$PathLocation')  # Appends a path for checking for modules  # Not best looking approach (Can add to environment variables of OS)

print(sys.path)

#- Order of checking
- Directory containing the script we are running
- Python path environment variable
- Then adds standard libraries Directory
- Site packages for third party packages

'''
# It Checks multiple locations for the imported modules - sys.path
'''
# The random - Standard Library
import random
courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)  # Returns a random chosen course for the list
'''

'''
#- Import underlying operating system
import os

print(os.__file__)  # Entire standard lib located. double underscore is known as dunder.
'''
