# Parent Class
class Employee:
    def __init__(self,id,name):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Id:- {self.id},Name:- {self.name}") 

Emp1 = Employee(21,"Adarsh")
Emp1.showDetails() 


# Child Class
#Here promoted Having the parent class qualities. Because in the paremeter it has the Employeee Class.
class promoted(Employee): 
        def ShowName(self):
            print(f"{self.name} is Promoted")

# Qualities of Parent class.
Emp2 = promoted(100,"Harveer") # It copies the Behaviour of their parent class and Itself has its own property which can only accessed by this class objects.
Emp2.showDetails()
Emp2.ShowName()