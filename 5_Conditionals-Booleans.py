'''
# Comparisons:
Equal:              ==
Not Equal:          !=
Greater Than:       >
Less Than:          <
Greater or Equal:   >=
Less or Equal:      <=
Object Identity:    is  # Verifies if the objects are the same in memory (have the same id)
'''

if True:
    print('Conditional was True')  # Executes if condition after if statement is true

if False:
    print('Conditional was True')  # Will not execute as condition is False

language = "Python"
#- If, elif, else statement (Python does not have a switch case statement)
if language == "Python":
    print('Langauge is Python')
elif language == "Java":
    print('Langauge is Python')
else:
    print("No match")

'''
# Boolean operations
and
or
not
'''

#- Using Boolean operations
user = "Admin"
loged_in = True

#- Using the 'and' keyword
if user == "Admin" and loged_in:
    print("Admin Page")
else:
    print("Bad Credentials!")

#-using the 'or' keyword
if user == "Admin" or loged_in:
    print("Admin Page")
else:
    print("Bad Credentials!")

#-using the 'not' keyword
if not loged_in:  # If not false
    print("Please Log In")
else:
    print("Welcome")

# Object Identity - Test if two objects has the same id
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))  # Returns id of a (Memory address)
print(id(b))  # Returns id of a (Memory address)
print(a == b)  # Evaluates to true
print(a is b)  # Evaluates to False as it does not have the same address/id's
b = a
print(a is b)  # Evaluates to True as it has the same address/id
print(id(a))  # Returns id of a (Memory address)
print(id(b))  # Returns id of a (Memory address)
print(id(a) == id(b))  # Evaluates to True as the id's match

'''
# False Values:
- False
- None
- Zero of any numeric type, all other values evaluates to True
- An empty sequence. E.g '', [], ()
- An empty mapping. E.g. {}
'''

condition = False
if condition:
    print("Evaluates to True")
else:
    print("Evaluates to False")
