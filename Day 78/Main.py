class Human:

    def __init__(self, name, gender):
        self.name = name;
        self.gender = gender



    def showName(self):
        print(f"The name of the Human is {self.name} Type {self.gender}")  


H1 = Human("Kartik" , "Male")
H1.showName()


# He we Inherit the properties of class Human in the Emp class which is the simple example of Single Inheritance.
class Emp(Human):
    def __init__(self ,name ,gender ,empId):
        # Here Just we have the need to call the Human class contructor becuase it was dynamically typed method which will help name and gender to initize dynamically at the runtime.
        Human.__init__(self ,name , gender)
        self.empId = empId

    def showDetail(self):
        print(f"Employee Id : {self.empId};\nName : {self.name};\nGender : {self.gender}")    

Emp1 = Emp("Adarsh","Male",1)