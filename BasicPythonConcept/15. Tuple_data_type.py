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

print("\n\n", "Practise of Built-in function of tuple data type".upper().center(160, '-'))

# count      index      len


# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# count element 'i'
count = vowels.count('i')
# print count
print('The count of i is:', count)
# count element 'p'
count = vowels.count('p')
# print count
print('The count of p is:', count)
# random tuple
random = ('a', ('a', 'b'), ('a', 'b'), [3, 4])
# count element ('a', 'b')
count = random.count(('a', 'b'))
# print count
print("The count of ('a', 'b') is:", count)
# count element [3, 4]
count = random.count([3, 4])
# print count
print("The count of [3, 4] is:", count)



# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)
# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')
print('The index of i:', index)
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'u')
# index of'p' is vowels
index = vowels.index('p')
print('The index of p:', index)

# other built-ins are :
# all()     any()       ascii()     bool()      enumerate()     filter()        iter()      len()       max()
# min()     map()       reversed()      slice()     sorted()        sum()       tuple()     zip()
