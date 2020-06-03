# Variables and types of variable in python.

a = "variable"  # here, a is the variable which holds the a string "variable".
print(a)

# Re-declare of variable :
a = 2048  # here, we re-declare variable-a with numeric value.
print(a)

# Different type of data cannot combine :
# a = "variable" + 2048   # it will generate TypeError
# print(a)
a = "variable" + "-a"  # it will not generate any error because we use same type of data.
print(a)

# Multiple Assignment of variable :
a = b = c = 10
print(a, b, c)
a, b, c = 101, 3.14, 'variable'
print(a, b, c)

# Deletion of  variable :
del a
# print(a)      # It will generate NameError
print("\n\n")

# Types of variables in python :
# 1.Global Variables : A variable declared outside of the function or in global scope is known as a global variable.
# This means that a global variable can be accessed inside or outside of the function.
# 2.Local Variables : A variable declared inside the function's body or in the local scope is known as a local variable.
# 3.Nonlocal Variables : Nonlocal variables are used in nested functions whose local scope is not defined.
# This means that the variable can be neither in the local nor the global scope.
# lets take an example :
print("Types of variable".center(50, '-'))
print("Example of local variable - ")
# declare a variable
variable = 101
print("variable value before function calling : ", variable)


def foo():
    variable = 20448  # here, it is a local variable of this function.
    print("variable value inside foo() : ", variable)


foo()
print("variable value after function calling : ", variable)

print("\nExample of global variable - ")
# declare a variable
variable = 101
print("variable value before function calling : ", variable)


def foo():
    global variable
    variable = 20448  # here, it is a local variable of this function.
    print("variable value inside foo() : ", variable)


foo()
print("variable value after function calling : ", variable)

# one more example on global and local variables :
print("\nExample of local and global variable - ")
variable_one = 101
variable_two = 2048


def fun():
    global variable_three
    variable_three = 5012
    print("Value of variable_one inside function before changing : ", variable_one)
    # print("Value of variable_two inside function before changing : ", variable_two)
    variable_two = 7890
    print("Value of variable_two inside function after changing : ", variable_two)
    print("Value of variable_three which declare and initialize as global inside function : ", variable_three)
    # variable_one = 2018   # This statement will generate UnboundLocalError: local variable 'variable_one' referenced
    # before assignment in line number 72.


fun()
print("Value of variable_three which declare and initialize as global inside function at outer : ", variable_three)
print("value of variable_one after function calling : ", variable_one)
print("value of variable_two after function calling : ", variable_two)


# non-local variable :
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

print("\n\n")
# class and instance variable :
# Class Variables — Declared inside the class definition (but outside any of the instance methods).
# Instance Variable — Declared inside the constructor method of class (the __init__ method).
class Car:
    wheels = 4    # <- Class variable

    def __init__(self, name):
        self.name = name    # <- Instance variable


jag = Car('jaguar')
fer = Car('ferrari')
print(jag.name, fer.name)
print(jag.wheels, fer.wheels)
print(Car.wheels)
print("\n\n")
# print(Car.name)
# AttributeError: type object 'Car' has no attribute 'name'
Car.wheels = 3
print(jag.wheels, fer.wheels)
Car.wheels = 4
jag.wheels = 3
print(jag.wheels, fer.wheels, Car.wheels)
print(jag.wheels, jag.__class__.wheels)



class Dog:
    kind = "canine"     # class variable shared by all instances.

    def __init__(self, name):
        self.name = name    # instance variable unique to each instances.


d = Dog('Fido')
e = Dog('Buddy')
print("d : ", d.kind)
print("d : ", d.name)
print("e : ", e.kind)
print("e : ", e.name)
e.kind = 'other'
print("e : ", e.kind)
print("\n\n")


# Private variable :
# private variables are those variables that can be visible and accessible only within the class they belong to and
# not outside the class or any other class.
# These variables are used to access the values whenever the program runs that is used to keep the data hidden
# from other classes.
# Since there is a valid use-case for class-private members there is limited support for such a mechanism,
# called name mangling.
# We use dunder as prefix of the variable to make it private variable of a class.
# examples :
class mainclass:
    __privateVariable = 2020;

    def __privateMethod(self):
        print("I'm inside class mainclass that is this is private method")

    def insideclass(self):
        print("Private Variable: ",mainclass.__privateVariable)
        self.__privateMethod()


foo = mainclass()
foo.insideclass()
# foo.__privateMethod()     # this statement will generate
# AttributeError: 'mainclass' object has no attribute '__privateMethod()'.


