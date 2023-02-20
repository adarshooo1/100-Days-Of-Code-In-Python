# Example 1:
class GrandFather:
    # Grand Father is the parent class:
    pass

class Father(GrandFather):
    # Father is the derived class from Grand Father.
    pass

class Son(Father):
    # Son class is the derived class and derived class itself is a derived class form Grand Father.
    pass



# Example 2:
class Human:
    def __init__(self, Name,Gender):
        self.Name = Name
        self.Gender = Gender

    def showEmpDetail(self):
        print(f"Name = {self.Name}\nGender = {self.Gender}")       

class Employee(Human):
    def __init__(self, EmpId , Name , Gender):
            Human.__init__(self , Name , Gender)
            self.EmpId = EmpId

    def showEmpDetail(self):
        print(f"Employee Id = {self.EmpId}\nName = {self.Name}\nGender = {self.Gender}")        

class Manager(Employee):
    def __init__(self, Position , EmpId , Name , Gender):
        Employee.__init__(self, EmpId , Name , Gender)
        self.Position = Position

    def showManagerDetail(self):
        print(f"Position = {self.Position}\nEmployee Id = {self.EmpId}\nName = {self.Name}\nGender = {self.Gender}")  



Manager1 = Manager("Managing Director" , "101" , "Adarsh" , "Male")
Manager1.showManagerDetail()
#This is the example of Multi-Level Inheritance in Python Where, Sub-base class Inherit the properties of the Base class, Base class Inherit the properties of the Parent class.