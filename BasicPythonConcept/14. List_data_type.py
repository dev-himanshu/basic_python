# list data-types with their built-in functions :
l = [1, 2, 3, 4, 5, "0.354"]
bif_of_list = dir(l)
print("\n\n", "Built-in function of list data".upper().center(160, '-'))
print("Total functions are : ", len(dir(l)))
for i in range(0, len(dir(l))):
    print(bif_of_list[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()

print("\n\n", "Practise of Built-in function of list data type".upper().center(160, '-'))

# append      clear      copy      count      extend      index     insert      pop      remove      reverse      sort
# len

