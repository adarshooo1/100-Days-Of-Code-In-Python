# # Example 1: dir()
# X = [1,2,3,4,5]
# print(dir(X))
# print(X.__add__)# A method of this list.

# Y = (1,2,3,4)
# print(dir(Y))

# Example 2: __dict__()
class Master:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

Human = Master("Adarsh", 20)
print(Human.__dict__) 


# the __ dict__() Method will print all the item in self method in the class.{'name': 'Adarsh', 'age': 20, 'version': 1}


# 3.help() -> The help() functions use to get help documentation for an object, indicating of its attributed and methods.
# Example:- 
# With the previous class Master we will use this help method
print(help(Master))

# output below this will give a ducumentation of the help.

# Help on class Master in module __ma
# in__:

# class Master(builtins.object)
#  |  Master(name, age)
#  |
#  |  # Example 2: __dict__()
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name, age)
#  |      Initialize self.  See help(
# type(self)) for accurate signature.
#  |
#  |  -------------------------------
# -----------------------------------
# ----
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance var
# iables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to

# None