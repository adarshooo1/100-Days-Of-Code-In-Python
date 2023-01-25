# Example 1:-
  #  is use cases:-
Value = 12
Value2 = "12"

print(Value is Value2) # False
# Because Weather is objects are written same but but differetly defined then it dosen't be same. Because data-types are different.

Value3 = 20
Value4 = 20

print(Value3 is Value4) # True 
# Because the objects are defined with different variable names but it is pointing to the same value. Like it stored in a pool of same object.Only in case of constant and tuple. Not is the case of Dict or list like here.

Value5 = 21
Value6 = 22

print(Value5 is Value6) # False
# Because the objects are Different and it is differently strored in a different valriable so it is false.

# Example 2:- 
  #  == use cases

obj = 12
obj2 = "12"
print(obj == obj2) # False
# Becuase variable are different and Datatypes are different.

print(obj == 12) # True
print(obj2 == "12") # True
# Because we are comparing with the same values.


obj3 = 13
obj4 = 14
print(obj3 == obj4) # False 
# Because variable are different as well as object.

obj5 = 15
obj6 = 15
print(obj5 == obj6) # True
# Because the objects are stored in same in a Integer pool

obj8 = "Adarsh"
obj7 = "Adarsh"
print(obj7 == obj8)# True
# Because the objects are same and stored in  a string pool.

print(obj7 is "Adarsh")# Error because object stored in a valriable can be same. But when we compare a object with a value then it is totally different because is compares with the same location of the objects.

