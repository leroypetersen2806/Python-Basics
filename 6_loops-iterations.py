'''
# Loops - Keywords
break - breaks out of loop
continue - Moves on to next iteration in the loop
'''

nums = [1, 2, 3, 4, 5]

#- Looping through list. Adds a new line after each item in the list
for num in nums:
    print(num)  # Looping through each value in the list (num = to next item in the list)

#- Sets end line to a space instead of \ns
for num in nums:
    print(num, end=' ')

#- Sets endline to a "-" instead of a newline
print('\n')
for num in nums:
    print(num, end='-')
print('\n')

#- Using break statement
for num in nums:
    if num==3:
        print("Found!")
        break  # Breaks out of the for loop
    print(num)

#- Using continue statement - Ignore value, but does not break out of loop
for num in nums:
    if num==3:
        print("Found!")
        continue  # Ignores value and does not print it out
    print(num)

#- Nested Loops
for num in nums:
    for letter in 'abc':
        print(num, letter)  # For each number will loop through all the chars in the string, prints out the num and char

#- Going through loops a certain number of times
for i in range(10):
    print(i)  # Returns 0 - 9

for i in range(1, 11):
    print(i)  # Start value 1 and end value 10 (11-1)

'''
# While Loops - Runs until a condition is met (break method)
'''
x = 0
while x<10:   # Will iterate forever until condition is met (In this case if x >= 10)
    print(x)
    x+=1

#- Can break out of loop using the break statement (use ctrl+c to break infinite loops)
while x<10:
    if x == 5:
        break
    print(x)
    x+=1

# - Comment highlighted lines by pressing ctrl+/
