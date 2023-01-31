Fruits = ["Apple", "Banana", "Grapes", "Pine-Apple"]

#Looping over a list
for a in Fruits:
    print(a)

# Looping over the List along with list items seperately
for b in Fruits:
    for c in b:
        print(c)

# Looping over the list with Enumerate function which will print the index as well
for d,Fruits in enumerate(Fruits):# If want to start count from 1 then: enumerate(Fruits,Starts = 1), This will start the counting form the index 1.
    print(d,Fruits)

# Run this Code By comment all code
# Looping and enumerate function using like this will return the output in class tuple. But the condition is to comment out the previous code to run this correctly
for E in enumerate(Fruits):
    print(E)

# Run thise Code By comment all code
# Here Looping with enumerate with the string formatting and indexing also
for F,Fruits in enumerate(Fruits):
    print(f"{F+1} : {Fruits}")
#    # print(type(Fruits))#Type of F is <class:int> and Fruit is <class:Str>


# Like this way we can also enumerate word by word,and Indexing also
Word = "Intelligent"
for z, Word in enumerate(Word,start=1):
    print(z,Word)
    



