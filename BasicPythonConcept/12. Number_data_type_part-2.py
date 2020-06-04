# number data types-complex with their built-in functions :

c = 4 + 5j
bif_of_complex = dir(c)
print("\n\n", "Built-in function of complex data".upper().center(160, '-'))
print("Total functions are : ", len(dir(c)))
for i in range(0, len(dir(c))):
    print(bif_of_complex[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()

# built-in function of complex type number data type :
print("\n\n", "Practise of Built-in function of complex data type".upper().center(160, '-'))
print(c.conjugate())
print(c.imag)
print(c.real)

