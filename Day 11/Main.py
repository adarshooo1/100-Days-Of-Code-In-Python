Str  = "This is a string"
print(Str)

Str2 = "This is Str 2"
print(Str2)

print(Str,Str2)

# Ex:- Print: He said,"I want to eat an apple

# Way 1:-
print('He said,"I want to eat an apple')
# Way 2:-
print("He said,\"I want to eat an apple")

# Escape Sequence in String
print("He is the Man\nof Words\tnot the bullshit")
# \n :- for new line.
# \t :- for tab space.

Apple = """A big red fruit
which is Sweet and juicy\nNice in taste and
some of the juice company like \tReal\tMaking apple juice"""
print(Apple)

# //////////////////////////////////////////
# Example 1:-
# Accessing Characters of a String
Name = "Adarsh"
print(Name[0])
print(Name[1])
print(Name[2])
print(Name[3])
print(Name[4])
print(Name[5])

# Example 2:-
# Accessing Character with for loop
for character in Name:
    print(character)
# It is like an array of character
# Array:-It means a collection of Items    

# Example 3:-
for character2 in Name:
    print(character2,end= ' ')
    # Print List items in a single line not in seperate line

# Example 4:-
for character3, char in enumerate(Name):
    print(character3,char) 
    # This will print string item with the index number
    # Ex:- 0 A
        #  1 d
        #  2 a
        #  3 r
        #  4 s
        #  5 h

# Example 5:-
# To get the length of the string or list item of a array then
print(len(Name))
# It will give the len of the apple,Where [len = (n-1)] in Indexing

# ////////////////////////////////////////
# We can also format string also:
Boy = "Adarsh"
Habbit = "Good"
print(f"{Boy} is a good boy and He is very {Habbit} in Study and Playing")