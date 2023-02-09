class parent:
    def parent_method(self):
        print("Adarsh is on parent method")

# This is the other class which is having the parent class in their parameter.
class ChildClass(parent):
    def child_Method(self):
        print("Adarsh Is On Child Mehtod")
        # This super() will call the properties of the parent mathod of the from the parent class.
        super().parent_method()

    def child_child_Mehtod(self):
        print("Adarsh is on the child child Method")
        # This super() will call the properties of the parent mathod of the from the parent class.
        super().parent_method()


Adarsh = ChildClass()
Adarsh.child_child_Mehtod()


Adarsh = ChildClass()
Adarsh.child_Method()

Adarsh = parent()
Adarsh.parent_method()




# Exmaple 2

class Employee:
    def __init__(self, name , id):
        self.name = name;
        self.id = id;


class Programmer:
    def __init__(self, name , id , lang):
        self.name = name ;
        self.id = id;
        self.lang = lang;


Stud1 = Employee("Adarsh", 21)
print(Stud1.name , Stud1.id)


Person1 = Programmer("Adrash Singh" , 12 , "JPython")
print(Person1.name , Person1.id , Person1.lang)


class Dry(Programmer): #Here we have extended the parent class from where we want to inherit the properties and Call this inside the parameter in the New class.
    def __init__(self , name , id , lang , Experience):
        # super().__init__ -> will class the parent init method.
        super().__init__(name , id , lang)
        # Now we have assigned the new value as well.
        self.Experience = Experience

Smart_Person = Dry("Dhruv" , 1991 , "Python" , "2 Years")
print(Smart_Person.id)
print(Smart_Person.name)
print(Smart_Person.lang)
print(Smart_Person.Experience) 

        


         

