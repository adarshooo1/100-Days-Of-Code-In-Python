# create an empty tuple
my_tuple = ()
print(type(my_tuple))

# create a tuple of integers
my_tuple2 = (1, 2, 3, 4, 5)

# create a tuple of mixed data types
my_tuple3 = (1, 'hello', 3.14, True)

# create a tuple of tuples
my_tuple4 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Create a tuple of a single element with 1.small braces and 2.small braces and ,
tup5 = (1)
print(type(tup5),tup5)#Type int

tup6 = (1,)
print(type(tup6),tup6)#Type tuple

tup7 = (1,2,3,4,5,6)
print(type(tup7))
print(tup7[2])#Here accessing the value of tup7 at index 2

# tuple type of mix element
tup8 = (2,"Adarsh",True,4,2.3,44444)
print(tup8)
# We can also do indexing to the element in tuple

# Using conditional in tuple
if "Adarsh" in tup8:
    print("It present")
else:
    print("It is Absent") 

#Creating a new tuple from a tup8 
tup9 = tup8[0:4]
print(tup9)

print(tup8[::2])#It basically print every 2nd element in the tuple
print(tup8[0:len(tup8):3])#Print the complete tuple at every 3rd indexing element