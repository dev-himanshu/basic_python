# keywords in python

import keyword
keywords = keyword.kwlist
print(keywords)
print("\nType of the output: ", type(keywords))
print("Number of keywords: ", len(keywords))

print("Does python have False keyword?\n", keyword.iskeyword("False"))
print("Does python have list keyword?\n", keyword.iskeyword("list"))
