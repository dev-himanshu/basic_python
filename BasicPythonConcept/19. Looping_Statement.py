# loop statement in python :
# There are mainly three types of loop -
# (a). Conditional Loop Statement, (b). Count Loop Statement  and (c). Sentinel Value Loop Statement

# In python, we can implement loop statement in two ways -
# 1. for loop.
# 2. while loop.

# for loop :
num = int(input("Enter a number : "))
for i in range(1, 11):
    print(f"{num} x {i} -->", num*i)

# while loop :
while num >= 0:
    print(num)
    num -= 1
