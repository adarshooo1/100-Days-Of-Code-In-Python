a = input("////Message////")
print(a)

print(type(a))
"""Here we tried to change the type of the reference value but still we are
not able to change the the datatype of the reference. Because we are taking input
in the String so but still stype caasting stuff is not able to change the value of the string
Datatype.(Case:- 1) So we can solve this problem to take input in the Desired type which we want.
Extensively we can do this by type casting the input promt. """

print(int(a))#Here we tried to typecast string to Integer.But It's not worked for me


print(type(a))# still it is showing Reference to value type string

#So lets solve this problem;


Number = int(input("////Message////"))# here we taking input as Integer and Explicetly we give command to python that just take input from user in the type Inetger with the help of type casting.

print(Number)
print(type(Number))# Type Integer❤️