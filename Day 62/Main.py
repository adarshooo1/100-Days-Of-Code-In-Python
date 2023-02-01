class Employee:
    pass

a = Employee()
a.emp1 = 12
print(a.emp1)

# In python every variable is public by defalut;


class Human:
    def __init__(self):
        self.name = "Adarsh"


emps = Human()
print(emps.name)


# Private Access Modifiers.
# How we can access this:
class Game:
    def __init__(self):
        self.__game = "Volley Ball"


games = Game()
# object name + class name with single underscore + function name with double underscore.
print(games._Game__game) #This concept is treated as private access modifier in java, So function and variable can only be access by the class name.

# print(games.__game) This will through error.


print(games.__dir__())#This __dir__() will give the information that what are the methods we can alpply on this object.

# Protected Access Modifiers

# In OOPS ,the term "Protected" is used to describe a member of a class that is intended to be accessed only by the class itself and its sub-class.
# In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example,f a class has a method called 
# _my_method, it is indicating that the method should be accessed by the class itself and its subclsss; 

class mobile:
    def __init__(self):
        self._mobile = "I hava a iphone 12 as a spare and Have 14 to show other"
        self._mobile2 = "I have a Android as well"

# This naming converntion we are use a protcted access modifiers but here name mangling concepts are working.
object = mobile()
print(object._mobile)
print(object._mobile2)
print(dir(object))
