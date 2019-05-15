### Lists (mutable[can be changed])- Allows us to work with a list of values
courses = ['History', 'Math', 'Physics', 'CompSci']  # List of courses
print(courses)  # Returns the list of courses
print(len(courses))  # returns the length of the list
print(courses[0])  # Returns first value of the list (index == 0)
print(courses[-1])  # Returns last value of the List
print(course[:2])  # Returns first two indexes
print(courses[2:])  # Return values from index 2 until the end of List
courses.append('Art')  # Append value Art at the end of the List
courses.insert(0, 'Art')  # Add value Art at position 0

courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)  # returns a new list at position 0 for List as a list

courses.append(courses_2)  # Appends the list as a list to last postion
courses.extend(courses_2)  # Extends the courses at the the last point.

courses.remove('Math')  # Removes Math from courses List
courses.pop()  # Removes last value of the list. (Also returns the last value remove, see below)
popped = courses.pop()  # Returns the last value popped.
print(popped)  # Returns the popped values

courses.reverse()  # Returns list in reversed order
courses.sort()  # Returns the list as shorted in alphabetical(for numbers will short in ascending order)
courses.sort(reverse=True)  # Returns list in descending order
sorted(courses)  # Keeps courses in the same order, but have return a sorted version of the List
sorted_courses = sorted(courses)  # Returns sorted version of the List
print(sorted_courses)

num = [1, 2, 3, 4, 5]
print(min(num))  # Return the minimum value in the list (1)
print(max(num))  # Return the minimum value in the list (5)
print(sum(num))  # Returns sum of numbers

print(courses.index('CompSci'))  # Returns the index of where CompSci is (index 3)
print('Art' in courses)  # Return Boolean if item is found in the list or not (False)

for course in courses:
    print(course)  # Returns the values in courses on a new line

for index, course in enumerate(courses):
    print(index, course)  # Returns the index and the value

for index, course in enumerate(courses, start=1):
    print(index, course)  # Returns the index and the value starting at index 1

course_str = ', '.join(courses)
print(course_str)  # Returns values comma separated

new_list = course.str.split(' - ')
print(new_list)  # Returns values as a list

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
list_1[0] = 'Art'
print(list_1)
print(list_2)  # Returns the same list as list_1 as they are both the same mutable object

### Tuple - Cannot be modified (immutable[cannot be changed])
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

tuple_1[0] = 'Art'
print(tuple_1)
print(tuple_2)  # Error 'tuple' object does not support item assignment (immutable)

### Sets - Values are unordered and has no duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}  # Does not return second 'Math'
print(cs_courses)  # Returns the values of the set, but not in the order added (order change with each execution)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))  # See intersection of courses (Math and History returned)
print(cs_courses.difference(art_courses))  # Returns the difference (Physics and CompSci)
print(cs_courses.union(art_courses))  # Returns all courses from both sets


### Creating Empty List, Tuples and Sets
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty sets
empty_set = {} # Incorrect as this creates a dictionary and not a sets
empty_set = set()
