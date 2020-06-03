# Formatting :
# Here are some basic argument specifiers you should know:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
name = 'himanshu'
age = 21
print("My name is %s and I am %d year old." % (name, age))
pi = 3.14159265358979
print("Value of pi is %f" % pi)
print("Value of pi is %.2f" % pi)


# f-string
print(f"My name is {name} and I am {age} old.")
print(f'{2*3}')


# format()
print("My name is {} and I am {} year old.".format(name, age))
print("My name is {0} and I am {1} year old.".format(name, age))
print("My name is {1} and I am {0} year old.".format(name, age))
print("My name is {f_name} and I am {u_age} year old.".format(f_name=name, u_age=age))
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))
print("The float number is:{:f}".format(123.4567898))
print("The float number is:{}".format(123.4567898))
print("The float number is:{:f}".format(123))
# integer numbers with minimum width
print("{:5d}".format(12))
# padding for float numbers
print("{:8.3f}".format(12.2346))
# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))
# Formatting dictionary members using format()
person = {'age': 23, 'name': 'Adam'}
print("{p[name]}'s age is: {p[age]}".format(p=person))
