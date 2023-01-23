from functools import reduce

# A function which will print square of a number.
cube = lambda x : x**2

Numbers = [1,2,3,4,5]

# Old way
newlist = [] #Create a new list.
for num in Numbers:
 newlist.append(cube(num))
print(newlist) 
  
# New way with map()
NewNumbers =list(map(cube,Numbers))# This map function taking function as a arguement.
print(NewNumbers)

# Filter()
# Example 1:
def filter_function(num):
  return num%2 == 0 # Return a Boolean Expression;
  
newlist2 = list(filter(filter_function,Numbers))
print(newlist2)# In form of list we are getting the answers so thats why we have to take newlist2 as a form of list first.

# Example 2:
Numbers2 = [2,3,4,5,6,7,8,9,10]
Even =filter(lambda x: x%2 == 0,Numbers2)
print(list(Even))

# Reduce()
Numbers3 = [20 ,30 ,40 ,20 ,30 ,40]
sum = (reduce(lambda x,y : x + y,Numbers3)) # Here it is simply reducing the size and sum all element inside the list.
print(sum)

