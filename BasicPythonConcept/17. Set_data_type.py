# set data-types with their built-in functions :
s = {"hello,", "this", "is", "0832cs171065"}
bif_of_set = dir(s)
print("\n\n", "Built-in function of set data".upper().center(160, '-'))
print("Total functions are : ", len(dir(s)))
for i in range(0, len(dir(s))):
    print(bif_of_set[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()

print("\n\n", "Practise of Built-in function of set data type".upper().center(160, '-'))

# add      clear      copy      difference      difference_update      discard      intersection
# intersection_update      isdisjoint      issubset      issuperset      pop      remove      symmetric_difference
# symmetric_difference_update      union      update    len


