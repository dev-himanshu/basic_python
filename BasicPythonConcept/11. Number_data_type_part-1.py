# number data types-int & float with their built-in functions :
a = 5
bif_of_int = dir(a)
print("\n\n", "Built-in function of int data".upper().center(160, '-'))
print("Total functions are : ", len(dir(a)))
for i in range(0, len(dir(a))):
    print(bif_of_int[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()

b = 3.14
bif_of_float = dir(b)
print("\n\n", "Built-in function of float data".upper().center(160, '-'))
print("Total functions are : ", len(dir(b)))
for i in range(0, len(dir(b))):
    print(bif_of_float[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()

