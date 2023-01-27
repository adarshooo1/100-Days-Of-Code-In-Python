# // Procedural Programming
def Greet(Name):
  print("Hello " + Name)


Greet("Adarsh")
Person1 = "Adarsh"
Married1 = False
Height1 = 5.9

Person2 = "Deepanshu"
Greet(Person2)
Married2 = False
Height1 = 5.10

Person3 = "Rahul"
Greet(Person3)
Married3 = True
Height3 = 5.6

# Like this way have to write so many lines of code,and OOPs can help in this case.

# With OOPs we can simply create a Template with the help of it. We can create as many objects as we want.


class Human():
  def __init__(self, Names, Age, Pet):  #Here __init__ is a keyword which will have the instance oh class Human.
    self.Names = Names  #Here we have the self keyword which will help in dynamically allot the object when they created.
    self.Age = Age
    self.Pet = Pet  
  # NOTE :- Here we are defining this function inside this functions of this class. inside
  def wishes(self): # Self is a keyword. which will take the Insance of the class.
        print("Today is Republic Day "+ self.Names) #Here in self.Names will access the Names with the help of self keyword.

Per1 = Human("Sneha", 18, "Dog")
print(Per1.Names)
print(Per1.Age)
print(Per1.Pet)
Per1.wishes()   #Here when we call the Per1 and wishes. with the help of . operator as the . operator help in to bind the function with the instance of the class.

Per2 = Human("Sopnil",20,"Cow")
print(Per2.Names)
print(Per2.Age)
print(Per2.Pet)
Per2.wishes()

