class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    def changeCompany(cls , newCompany):
        cls.company = newCompany



Emp1 = Employee()
Emp1.name = "Adarsh"
Emp1.show()


Emp1 = Employee()
Emp1.name = "Adarsh"
Emp1.show()
Emp1.changeCompany("Google") #Here we changed the company name, but still this is change for this onject only not for that others
print(Employee.company) # But still the company name is not changed for the class variable.


class Employee2:
    Company2 = "Ienergizer"
    def stud(self):
        print(f"The Employee name is {self.name} and the company name is {Employee2.Company2}")

    @classmethod #This will help in to manipulate the class variable. With @classmethod
    def changecompanyName(cls ,newCompany2):
        cls.Company2 = newCompany2     

Emp2 = Employee2()
Emp2.name = "Raghav"
Emp2.stud()
Emp2.changecompanyName("Samsung")
Emp2.stud()

print(Employee2.Company2)



