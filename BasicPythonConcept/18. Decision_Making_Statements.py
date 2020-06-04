# Decision Making Statement :
# There are three types of decision making statement --
# 1. if
# 2. if...else
# 3. if...elif...else


# if statement :
break_point = int(input("Enter any breakpoint to break loop : "))
for i in range(1, break_point+1):
    print("Value of i :", i)
    if i == break_point:
        print("Loop exit.")


# if...else statement :
num_one = float(input("Enter first number : "))
num_two = float(input("Enter second number : "))
if num_one > num_two:
    print(f"{num_one} is greater than {num_two}.")
else:
    print(f"{num_two} is greater than {num_one}.")


# if...elif...else statement :
age = int(input("Enter first number : "))
if (age < 12) and (age > 0):
    print("You are kid.")
elif (age < 18) and (age > 12):
    print("You are teenager.")
elif age > 18:
    print("You are adult.")
else:
    print("Inappropriate input.")

# nested decision making statement :
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
