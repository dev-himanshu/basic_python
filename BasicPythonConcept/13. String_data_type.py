# string data-types with their built-in functions :
s = "hello, This is himanshu mishra"
s1 = "HIMANSHU MISHRA"
bif_of_string = dir(s)
print("\n\n", "Built-in function of string data".upper().center(160, '-'))
print("Total functions are : ", len(dir(s)))
for i in range(0, len(dir(s))):
    print(bif_of_string[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()

# capitalize      casefold      center      count      encode      endswith      expandtabs      find
# format      format_map      index      isalnum      isalpha      isascii      isdecimal      isdigit
# isidentifier      islower      isnumeric      isprintable      isspace      istitle      isupper      join      ljust
# lower      lstrip      maketrans      partition      replace      rfind      rindex      rjust      rpartition
# rsplit      rstrip      split      splitlines      startswith      strip      swapcase      title      translate
# upper      zfill

print("\n\n", "Practise of Built-in function of string data type".upper().center(160, '-'))
print(s.capitalize())
print(s1.casefold())
print(s.casefold())
print("THIS IS".casefold())
print(s.center(150, '-'))
print(s.count('i'))
print(s.encode('UTF-8', "i don't what to pass error."))
print(s.endswith('ra', 0, 5))
print(s.endswith('ra'))

