"""This module does meh"""


def main():
    """ This class runs the main program"""
    print("Hello World!")
    x_value = 10
    print(x_value)

    message = "Hello World"
    print(message)  # slicing
    print(message[0:5])  # Starting at 0 ending at 5-1
    print(message.lower())  # Setting upper to lower
    print(message.upper())  # Setting lower to upper
    print(message.count("Hello"))  # Search how many times input appears
    print(message.find("World"))  # Returns how many times word appears (-1 if none)

    message = message.replace(
        "World", "Universe"
    )  # Return a new string with value replaced

    message = message.replace("a", "b")
    print(message)
    ### Concatenation of strings
    greeting = "Hello"
    name = "Leroy"
    message = greeting + name  # No space added
    message = greeting + ", " + name + ". Welcome!"  # Added the , and space
    message = "{}, {}. Welcome!".format(greeting, name)
    message = f"{greeting}, {name.upper()}. Welcome!"

    print(dir(name))  # Shows all attributes and methods has access to
    print(help(str))  # Display manual for string variables
    print(help(str.lower))  # Display method_description just on lower method


main()
