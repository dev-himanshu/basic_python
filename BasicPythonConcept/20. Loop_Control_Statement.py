# Loop Control Statement.
# There are two types of loop control statement - (a). break and (b). continue.

# break :
num = int(input("Enter breakpoint of loop : "))
for i in range(999999999999):
    print(i)
    if i == num:
        print("exit from loop.")

# continue :
num = int(input("Enter a point at which you want to skip (less than 10) : "))
for i in range(10):
    print(i)
    if i == num:
        continue
