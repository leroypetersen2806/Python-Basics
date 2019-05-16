'''
# Dictionaries allows us to work with KeyValuePairs [Hashmaps, associative arrays]
# Two link values where key is a unique identifier and value is the data
# Keys can be any immutable data type ['string', 'integers', 'lists', etc]
'''

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

# Accessing Keys
print(student['name'])  # Returns the key "name"

# Key as integer
student_int =  {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student_int[1])  # Will return the key "1"

# Best practice to check invalid Keys
print(student.get('phone', 'Not Found!'))  # Returns "Not Found!" if key invalid [default returns: None]

# Adding new entry to dictionary
student['phone'] = '555-5555'
print(student.get('phone', 'Not Found!'))

# Updating Values
student['name'] = 'Jane'
print(student['name'])  # Update key 'name' to 'Jane'

# Updating multiple Keys
student.update({'name': 'Leroy', 'age': 34, 'phone': '555-5555'})
print(student)  # Returns update key values

# Delete a key and its values
del student['age']
print(student)  # Removed they key 'age'
#- Can also use the pop method
name = student.pop('name')
print(name)  # Returns the name popped from the dictionary

# Returning keys, values or both
#- Getting length of dictionary
print(len(student))
#- Displaying only the Keys
print(student.keys())
#- Displaying only the Values
print(student.values())
#- Displaying keys and Values
print(student.items())  # Returns pairs of the key and Values

# Looping through keys and Values
for key in student:
    print(key)  # Returns only the keys in the dictionary
for value in student.values():
    print(value)  # Returns values in dictionary
for key, value in student.items():
    print(key, value)  # Returns the key and the value
