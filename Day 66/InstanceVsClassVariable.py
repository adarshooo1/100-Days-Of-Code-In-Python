# Example 1:
class Employee:

    companyName = "Google;" #This is act like a global vaiable which is the instance of the class.

    def __init__(self,name):
        self.name = name #Name is the instance of the class.
        self.income = 120000 #Income is the instance of that the function which means instanc of instance.

    def showDetail(self):
        print(f"The name of the employee is {self.name} He is working {self.companyName} and his income is {self.income}")

Obj1 = Employee("Adarsh")
Employee.showDetail(Obj1) # We can call the method by class name.
Obj1.showDetail() #We can also call by this which the help of the object.


# Exmaple 2
Obj1.income = 2000000
print(Obj1.income)


class Fun:

    NumberOfPlayer = 0

    Player = "Team India" #This refers to the class instance as we can see it is not defined with the function of the calss, This Itself is the instance of the class and It will act like a global variable.

    def __init__(self, name):
       self.name = name 
       self.sports = "Sports" #Self.sports is the instance of the instance
       self.fee = 1000
       Fun.NumberOfPlayer += 1 #Here we will call this with with the help if calss name, because it is not the instance of a function, Instead it is a instacne if a class.As more we make the object of this class then it will add add and increase the count of the object. with +1.
    
    #This is a change name function which will take name as a argument and will change the name of the existing student of student want to change his name.
    def changeName(self ,name):
        self.name = name   
    
    def showStudents(self):
        print(f"Number of Player {Fun.NumberOfPlayer} The student name is {self.name}. He is playing {self.sports} and the fee is {self.fee} and he is a player of {self.Player}")
                           #  Above It will increase the count as the object is created with the help of the object.
# Object 1;
Player1 = Fun("Adarsh")
Player1.sports = "VolleyBall" #We can change then also.
Player1.fee = 1200
Player1.showStudents()

# ChangeName function
Player1.changeName("Abhishek")
print(Player1.name)

Player1.showStudents()

# Object 2;
Player2 = Fun("De Villiars")
Player2.Player = "South Africa" #With this we can change the instance of the class because That was a default if object have their player instance Variable then it will print that instance else it will take the class isntance.We can print it explicitly or implicitly what ever we want.
Player2.sports = "Cricket"
Player2.fee = 100000
Player2.showStudents()

print(Player2.NumberOfPlayer) #Output = 2;
print(Player1.NumberOfPlayer) #An it is kind of static which is same for the every object of this class.

