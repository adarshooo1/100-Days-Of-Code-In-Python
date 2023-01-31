set1 = {1, 2, 3, 1, 2, 3, 4}
print(type(set1))
print(set1)#In sets weather the count of sny number can be more than one. Means,multiple occurance of a number or a object,So It will count only single time in the set

set2 = set()
print(type(set2))# Like this way we can create a empty set

set3 = {"Adarsh", "Dalra", 23, 3232.32, True, "Adarsh", 23}# It is a example of Mix set.
print(set3)#No gurantee of the order

set4 = {1}
print(type(set4))#Set of single item

set5 = {"Adarsh","D",2,23,244444,342.3333,2,2}
for num in set5:
  print(num)