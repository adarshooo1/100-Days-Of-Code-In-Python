# regular expression is a inbuilt module so just we have to import.
import re

# # Here we can give word to search
# pattern = "CSS works"

# string = '''Tailwind CSS works by scanning all of your HTML files, JavaScript components, and any other templates for class names, generating the corresponding styles and then writing them to a static CSS file.

# It's fast, flexible, and reliable — with zero-runtime. Regular Erpression,or "regex" for short, are a powerful tool for working with strings and text data in Python.
# They allow you to match and manipulate strings based on patterns, making it easy to perform complex string
# operations with just few lines of code. '''


# # Example 1:
# # Here we have search with the help of re module in the doc string of Python. Example:- re.search(word/pair of words , string) wich means search the word with in the string
# match = re.search(pattern , string)
# print(match)
# # output :-<re.Match object; span=(38, 41), match='you'>







# Example 2:
# In the parameter {r"[a-z or A-Z]works"} put any word in this place between these parameter and join the word which is after the parameter but before this convert into the raw string.
patter2 = r"[a-z or A-Z]orks"

string2 = '''Tailwind CSS Works by scanning all of your HTML files, JavaScript components, and any other templates for class names, generating the corresponding styles and then writing them to a static CSS file.

It's fast, flexible, and reliable — with zero-runtime. Regular Erpression,or "regex" for short, are a powerful tool for working with strings and text data in Python.
They allow you to match and porks manipulate strings based on patterns, making it easy to perform complex string
operations with just few lines of code. '''

match2 = re.search(patter2 , string2)
print(match2)
# output:- <re.Match object; span=(13, 18), match='Works'>. This will only search till the first reslut.

match3 = re.finditer(patter2 , string2)
for matches in match3:
    print(matches)
# output:-  <re.Match object; span=(13, 18), match='Works'> <re.Match object; span=(394, 399), match='porks'>   
