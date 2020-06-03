# Indexing and Slicing :

# indexing :
string = 'abcdefghijklmno'
# here, indexing is : a->0, b->1, c->2,....,o->14 and 0->-1, n->-2, m->-3,...., a->-15
print(string[0])
print(string[14])
print(string[-1])
print(string[-15])


# slicing
string = 'abcdefghijklmno'
# here, slicing is : string[start:end:step]
print(string[::])
print(string[0::])
print(string[1::])
print(string[:5:])
print(string[::2])
print(string[::-1])
print(string[-5:-10:-1])
print(string[-2::-1])
print(string[:-8:-1])

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(my_list[:5])
my_list = [
    [10, 20, 30],
    [40, 50, 60],
    [90, 80, 70],
]
print(my_list[1][:2])
