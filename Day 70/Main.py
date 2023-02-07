class Employee:
    def __init__(self, name , salary):
        self.name = name;
        self.salary = salary;
    
    @classmethod #This is also working as a constructor still its a class method.
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))




Emp = Employee("Adarsh" , 120000);    
print(Emp.name , Emp.salary)

# Example 2:
# If by chance we  get deta in string and then we have to extract those into the name and value.

string = "Adarsh-10000"
Emp2 = Employee(string.split("-")[0], int(string.split("-")[1]))
print(Emp2.name)
print(Emp2.salary)
# But what would if we have to for the large number or input.So we will use class Method as the alternative constructor.We will see this with the @classmethod


String2 = "Deepanshu-100000"
Emp3 = Employee.fromStr(String2)
print(Emp3.name)
print(Emp3.salary)