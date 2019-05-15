### Intergers and floats (Uses order of operations)
num = 3
print(type(num))  # Returns the class type <class 'int'>
num = 3.14
print(type(num))  # Returns the class type <class 'float'>

### Arithmetic Operators:
Addition:       3 + 2   # Adding the two values
Subtraction:    3 - 2   # Subtracting the two values
Multiplication: 3 * 2
Division:       3 / 2
Floor Division: 3 // 2  # Return floor division (No decimal)
Exponent:       3 ** 2  # Exponent and power (3^2)
Modulus:        3 % 2   # Returns the remainder after division (Check if number even or odd)

### Increment values
num = 1
num += 1  # Shorthand operations
num *= 10
print(abs(-2))  # Returns absolute values
print(round(3.75))  # Rounds up the values
print(rount(3.75, 1))  # Round to first digit after decimal

### Comparison Operators
Equal:              3 == 2
Not Equal:          3 != 2
Greater Than:       3 > 2
Less Than:          3 < 2
Greater or Equal:   3 >= 2
Less or Equal:      3 <= 2

num_1 = 3       # One = is assignment, two is comparison
num_2 = 2
print(num_1 == num_2)  # Will return True of False

num_1 = "100"  # These are strings not numbers
num_2 = "200"
print(num_1 + num_2)  # This will concatenate the two strings
num_1 = int(num_1)    # Casting values from string to integers
num_2 = int(num_2)    # Casting values from string to integers
print(num_1 + num_2)
