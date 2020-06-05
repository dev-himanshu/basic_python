# dict data-types with their built-in functions :
d = {1: "one", "two": 2, 3: ["index", "third"]}
bif_of_dict = dir(d)
print("\n\n", "Built-in function of dict data".upper().center(160, '-'))
print("Total functions are : ", len(dir(d)))
for i in range(0, len(dir(d))):
    print(bif_of_dict[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()

print("\n\n", "Practise of Built-in function of dict data type".upper().center(160, '-'))

# clear      copy      fromkeys      get      items      keys      pop      popitem      setdefault      update
# values    len

