# string data-types with their built-in functions :
s = "Hello, This is Himanshu Mishra 0832CS171065."
bif_of_string = dir(s)
print("\n\n", "Built-in function of string data".upper().center(160, '-'))
print("Total functions are : ", len(dir(s)))
for i in range(0, len(dir(s))):
    print(bif_of_string[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()



