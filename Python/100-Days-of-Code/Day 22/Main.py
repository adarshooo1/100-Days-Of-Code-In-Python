# create an empty list
my_list1 = []
print(type(my_list1))

# create a list of integers
my_list2 = [1, 2, 3, 4, 5]
print(my_list2[0])  # 1

# access the last element
print(my_list2[-1])  # 5

# access the third element
print(my_list2[2])  # 3

# access the second and third elements
print(my_list2[1:3])  # [2, 3]

# search of number in list.
#   With the help of conditional we can search the element of the which return the Boolean Expression.
if 3 in my_list2:#Find Integer in a list
    print("YES")
else:
    print("NO")    

if "3" in my_list2:
    print("Yes")
else:
    print('No')    


# create a list of mixed data types
my_list3 = [1, 'hello', 3.14, True]

# create a list of lists
my_list4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Create a list of type String
Str = ["Harry"]
if "Ha" in Str:
    print("Yes")
else:
    print("No")   

#Jump index
my_list5 = [2,5,7,9,10,12,13,14,15,16,20]
print(my_list5[:len(my_list5):2])#So, Here it is print from 0th index to the length of the list over the gap of 2.

# Comprehension List
my_list6 = [nums for nums in range(20)if nums%2 == 0]
print(my_list6)

# Putting values in list through for loop.
list = []
for i in range(10):
  if i%2 == 0:
    list.append(i)
print(list)