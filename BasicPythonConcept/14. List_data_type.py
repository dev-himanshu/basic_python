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

# animals list
animals = ['cat', 'dog', 'rabbit']
# 'guinea pig' is appended to the animals list
animals.append('guinea pig')
# Updated animals list
print('Updated animals list: ', animals)
# animals list
animals = ['cat', 'dog', 'rabbit']
# list of wild animals
wild_animals = ['tiger', 'fox']
# appending wild_animals list to the animals list
animals.append(wild_animals)
print('Updated animals list: ', animals)


# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]
# clearing the list
list.clear()
print('List:', list)
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]
# clearing the list
del list[:]
print('List:', list)


old_list = [1, 2, 3]
new_list = old_list
# add an element to list
new_list.append('a')
print('New List:', new_list)
print('Old List:', old_list)
# mixed list
my_list = ['cat', 0, 6.7]
# copying a list
new_list = my_list.copy()
print('Copied List:', new_list)
# shallow copy using the slicing syntax
# mixed list
list = ['cat', 0, 6.7]
# copying a list using slicing
new_list = list[:]
# Adding an element to the new list
new_list.append('dog')
# Printing new and old list
print('Old List:', list)
print('New List:', new_list)


# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# count element 'i'
count = vowels.count('i')
# print count
print('The count of i is:', count)
# count element 'p'
count = vowels.count('p')
# print count
print('The count of p is:', count)
# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
# count element ('a', 'b')
count = random.count(('a', 'b'))
# print count
print("The count of ('a', 'b') is:", count)
# count element [3, 4]
count = random.count([3, 4])
# print count
print("The count of [3, 4] is:", count)


# language list
language = ['French', 'English']
# another list of language
language1 = ['Spanish', 'Portuguese']
# appending language1 elements to language
language.extend(language1)
print('Language List:', language)
# language list
language = ['French']
# language tuple
language_tuple = ('Spanish', 'Portuguese')
# language set
language_set = {'Chinese', 'Japanese'}
# appending language_tuple elements to language
language.extend(language_tuple)
print('New Language List:', language)
# appending language_set elements to language
language.extend(language_set)
print('Newer Language List:', language)
a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)
# a1 = [1, 2, 3, 4]
a1.extend(b)
# a2 = [1, 2, (3, 4)]
a2.append(b)


# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)
# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')
print('The index of i:', index)
# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']
# index of'p' is vowels
# index = vowels.index('p')
print('The index of p:', index)
# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index)
# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)
# 'i' between 3rd and 5th index is searched
# index = alphabets.index('i', 3, 5)   # Error!
print('The index of i:', index)



# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']
# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)
# Updated List
print('Updated List:', languages)
# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
# remove and return the last item
print('When index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)
# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)
# remove and return the third last item
print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)



# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# 'rabbit' is removed
animals.remove('rabbit')
# Updated animals List
print('Updated animals list: ', animals)
# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
# 'dog' is removed
animals.remove('dog')
# Updated animals list
print('Updated animals list: ', animals)
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# Deleting 'fish' element
# animals.remove('fish')
# Updated animals List
print('Updated animals list: ', animals)



# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
# List Reverse
systems.reverse()
# updated list
print('Updated List:', systems)
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
# Reversing a list
#Syntax: reversed_list = systems[start:stop:step]
reversed_list = systems[::-1]
# updated list
print('Updated List:', reversed_list)



# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels.sort()
# print vowels
print('Sorted list:', vowels)
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
# The sort() method accepts a reverse parameter as an optional argument.
# Setting reverse = True sorts the list in the descending order.
vowels.sort(reverse=True)
# print vowels
print('Sorted list (in Descending):', vowels)
# take second element for sort
def takeSecond(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
random.sort(key=takeSecond)
# print list
print('Sorted list:', random)



print(len([10, 20, 30, 40, 50, 55, 60, 50]))


# list comprehension :
# generally, we do this.
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)
# by using list comprehension technique.
# syntax : [expression for item in list]
h_letters = [letter for letter in 'human']
print(h_letters)
# conditional in list comprehension.
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

# one more technique for list ; string to list.
# input format :
# 1
# 2 3 45 58
n = int(input("Enter input : "))
array_values = input("Enter array elements space separated : ").strip().split()
array_elements = [int(i) for i in input().split()][:n]
print("input value : ", n)
print("array values : ", array_values)
print("array elements : ", array_elements)

