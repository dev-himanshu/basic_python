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
print("This is \t python learning tutorial.".expandtabs(20))
print(s.find("is"))
print(s.find("is", 0, 10))
print("Hey, I am {}".format("Himanshu Mishra"))
dictionary = {'x': 54, 'y': 52}
print("Values are {x} and {y}".format_map(dictionary))  # The format_map() takes a single argument mapping(dictionary).
print(s.index('h'))
# print(s.index('i', 3, 8))                     # It raise error when not found any sub-string.
print("0832cs171065".isalnum())
print("This is 0832cs171065".isalnum())
print("0832cs171065".isalpha())
print("HimanshuMishra".isalpha())
print("Himanshu Mishra".isalpha())
print("hi".isascii())
print("08468".isdecimal())
print("hi".isdecimal())
print("hello!".isdigit())
print("08468".isdigit())
str = 'Python'
print(str.isidentifier())  # used to find valid identifier or not according to the defined rules of declaring identifier
str = 'Py thon'
print(str.isidentifier())
str = '22Python'
print(str.isidentifier())
str = ''
print(str.isidentifier())
print("hey".islower())
print("Hey".islower())
print("hello!".isnumeric())
print("08468".isnumeric())
s = 'Space is a printable'
print(s)
print(s.isprintable())
s = '\nNew Line is printable'
print(s)
print(s.isprintable())
s = ''
print('\nEmpty string printable?', s.isprintable())

print(" ".isspace())
print(s.isspace())
print("     ".isspace())
print("\t".isspace())
print("Himanshu Mishra".istitle())
print("Himanshu mishra".istitle())
print("HIMANSHU".isupper())
print("Himanshu Mishra".join("i don't know what string i should pass."))
# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))
# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))
s1 = 'abc'
s2 = '123'
# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))
# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))

string = 'cat'
width = 5
fillchar = '*'
# print left justified string
print(string.ljust(width, fillchar))

print("Himanshu Mishra".lower())


random_string = '   this is good '
# Leading whitepsace are removed
print(random_string.lstrip())
# Argument doesn't contain space
# No characters are removed.
print(random_string.lstrip('sti'))
print(random_string.lstrip('s ti'))
website = 'https://www.programiz.com/'
print(website.lstrip('htps:/.'))


# maketrans() : maketrans() creates a mapping of the character's Unicode ordinal to its corresponding translation.
# example dictionary
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))
dict = {97: "123", 98: "456", 99: "789"}
string = "abc"
print(string.maketrans(dict))
# first string
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString, secondString))


string = "Python is fun"
# 'is' separator is found
print(string.partition('is '))
# 'not' separator is not found
print(string.partition('not '))
string = "Python is fun, isn't it"
# splits at first occurence of 'is'
print(string.partition('is'))


song = 'cold, cold heart'
# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))
song = 'Let it be, let it be, let it be, let it be'
# replacing only two occurences of 'let'
print(song.replace('let', "don't let", 2))


quote = 'Do small things with great love'
# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))
# Substring is searched in ' small things with great love'
print(quote.rfind('t', 2))
# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))
# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))


quote = 'Do small things with great love'
# Substring is searched in ' small things with great love'
print(quote.rindex('t', 2))
# Substring is searched in 'll things with'
print(quote.rindex('th', 6, 20))
# Substring is searched in 'hings with great lov'
# print(quote.rindex('o small ', 10, -1))       # generate error


# example string
string = 'cat'
width = 5
fillchar = '*'
# print right justified string
print(string.rjust(width, fillchar))

string = "Python is fun"

# 'is' separator is found
print(string.rpartition('is '))
# 'not' separator is not found
print(string.rpartition('not '))
string = "Python is fun, isn't it"
# splits at last occurence of 'is'
print(string.rpartition('is'))


text= 'Love thy neighbor'
# splits at space
print(text.rsplit())
grocery = 'Milk, Chicken, Bread'
# splits at ','
print(grocery.rsplit(', '))
# Splitting at ':'
print(grocery.rsplit(':'))
grocery = 'Milk, Chicken, Bread, Butter'
# maxsplit: 2
print(grocery.rsplit(', ', 2))
# maxsplit: 1
print(grocery.rsplit(', ', 1))
# maxsplit: 5
print(grocery.rsplit(', ', 5))
# maxsplit: 0
print(grocery.rsplit(', ', 0))


text = 'Love thy neighbor'
# splits at space
print(text.split())
grocery = 'Milk, Chicken, Bread'
# splits at ','
print(grocery.split(', '))
# Splitting at ':'
print(grocery.split(':'))
grocery = 'Milk, Chicken, Bread, Butter'
# maxsplit: 2
print(grocery.split(', ', 2))
# maxsplit: 1
print(grocery.split(', ', 1))
# maxsplit: 5
print(grocery.split(', ', 5))
# maxsplit: 0
print(grocery.split(', ', 0))


grocery = 'Milk\nChicken\r\nBread\rButter'
print(grocery.splitlines())
print(grocery.splitlines(True))
grocery = 'Milk Chicken Bread Butter'
print(grocery.splitlines())


text = "Python is easy to learn."
result = text.startswith('is easy')
# returns False
print(result)
result = text.startswith('Python is ')
# returns True
print(result)
result = text.startswith('Python is easy to learn.')
# returns True
print(result)
text = "Python programming is easy."
# start parameter: 7
# 'programming is easy.' string is searched
result = text.startswith('programming is', 7)
print(result)
# start: 7, end: 18
# 'programming' string is searched
result = text.startswith('programming is', 7, 18)
print(result)
result = text.startswith('program', 7, 18)
print(result)


string = '  xoxo love xoxo   '
# Leading and trailing whitespaces are removed
print(string.strip())
# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))
# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))
string = 'android is awesome'
print(string.strip('an'))


# example string
string = "THIS SHOULD ALL BE LOWERCASE."
print(string.swapcase())
string = "this should all be uppercase."
print(string.swapcase())
string = "ThIs ShOuLd Be MiXeD cAsEd."
print(string.swapcase())


text = 'My favorite number is 25.'
print(text.title())
text = '234 k3l2 *43 fun'
print(text.title())


# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"
string = "abcdef"
print("Original string:", string)
translation = string.maketrans(firstString, secondString, thirdString)
# translate string
print("Translated string:", string.translate(translation))
# translation table - a dictionary
translation = {97: None, 98: None, 99: 105}
string = "abcdef"
print("Original string:", string)
# translate string
print("Translated string:", string.translate(translation))


# example string
string = "this should be uppercase!"
print(string.upper())
# string with numbers
# all alphabets whould be lowercase
string = "Th!s Sh0uLd B3 uPp3rCas3!"
print(string.upper())


text = "program is fun"
print(text.zfill(15))
print(text.zfill(20))
print(text.zfill(10))
number = "-290"
print(number.zfill(8))
number = "+290"
print(number.zfill(8))
text = "--random+text"
print(text.zfill(20))


print(len("this is string"))
