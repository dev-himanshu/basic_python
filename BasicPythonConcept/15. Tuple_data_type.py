# tuple data-types with their built-in functions :
t = (1, 2, 3, 4, 5)
bif_of_tuple = dir(t)
print("\n\n", "Built-in function of tuple data".upper().center(160, '-'))
print("Total functions are : ", len(dir(t)))
for i in range(0, len(dir(t))):
    print(bif_of_tuple[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()
