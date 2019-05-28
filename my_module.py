'''
# Importing Modules
'''
print('Imported my_module...')
test = "Test String"

def find_index(to_search, target):  # to_search - list to search, and target looking for
    '''Find the index of a value in a sequence'''   # Function documentation
    for i, value in enumerate(to_search):
        if value == target:
            return i  # Returns the found index
    return -1  # If not found, returns -1
