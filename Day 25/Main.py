# Indexing starts from 0
tuple = (1, 2, 3, 4, 5)
print(tuple[0])  # Output: 1
print(tuple[2])  # Output: 3


# Slicing:

tuple = (1, 2, 3, 4, 5)
new_tuple = tuple[1:3]  # Output: (2, 3)
new_tuple = tuple[:3]   # Output: (1, 2, 3)
new_tuple = tuple[1:]   # Output: (2, 3, 4, 5)


# Concatenation:

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 6)


# Repetition:

tuple = (1, 2)
new_tuple = tuple * 3  # Output: (1, 2, 1, 2, 1, 2)


# Membership:

tuple = (1, 2, 3, 4, 5)
print(1 in tuple)  # Output: True
print(6 in tuple)  # Output: False


# Length:

tuple = (1, 2, 3, 4, 5)
print(len(tuple))  # Output: 5


# Comparison:

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 2, 4)

print(tuple1 == tuple2)  # Output: True
print(tuple1 == tuple3)  # Output: False
print(tuple1 < tuple3)   # Output: True
print(tuple1 > tuple3)   # Output: False