# this is single-line comments in python

b = """This is doc-strings in python or it also known as multi-line comments"""
print(b)
print(type(b))
print(dir(b))
print(len(dir(b)))


def function_name():
    '''this is doc-strings in python'''
    return 'hello'


print(function_name())
print(function_name.__doc__)
print()
# print(function_name().__doc__)  # it will return full-documentation of this function.
print(function_name.__module__)
print(function_name.__annotations__)
print(print.__doc__)


# Here, we can see that the documentation of the print() function is present as the __doc__ attribute of this function.

# Python docstrings are the string literals that appear right after the definition of a function, method, class
# or module.

# 1. Docstrings for Python Modules
# The docstrings for Python Modules should list all the available classes, functions, objects and exceptions that are
# imported when the module is imported.
# They should also have a one-line summary for each item.
# They are written at the beginning of the Python file.

# 2. Docstrings for Python Functions
# The docstring for a function or method should summarize its behavior and document its arguments and return values.
# It should also list all the exceptions that can be raised and other optional arguments.
def add_binary(a, b):
    '''
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    binary_sum = bin(a + b)[2:]
    return binary_sum


print(add_binary.__doc__)


# 3. Docstrings for Python Classes
# The docstrings for classes should summarize its behavior and list the public methods and instance variables.
# The subclasses, constructors, and methods should each have their own docstrings.


class Person:
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, name, surname, age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        """

        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """

        print(f'My name is {self.name} {self.surname}. I am {self.age} years old.' + additional)


print(Person.__doc__)
help(Person)    # this is more convenient way to understand the use of any class or function with its body.

# Read Docstrings with the help() function
help(function_name)
