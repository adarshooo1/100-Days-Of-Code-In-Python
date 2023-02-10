class Employee:
    name = "Adarsh"

    def __len__(self):
        count = 0;
        for num in self.name:
            count += 1;
        return count;

    def __str__(self):
        return f"The name of the Employee is {self.name}"
            

Emp1 = Employee()
# It Simply called the class and the value inside the class.
print(Emp1.name)

# Now if we want to call the length then it will give error
print(len(Emp1)) #Her is is giving error to print the len,but when we use the len with Emp1.name then it will call the len method and tell the length

# Here we using the len method for the class.name
print(len(Emp1.name))

# What if we want to call our len method. Lets try
Emp2 = Employee();
Emp2.name = "Snachit Skowkeen" # Here we have changed the default name.
print(Emp2.name)

print(len(Emp2)) # Here we don't have the need to call those methods from thier full name like __len__ , instead of that we have only called here len(Emp2). Thatss why we called as Magic method.



# Example 2: In the Main2.py => where we will import this Employee class and see how str works.
class Tester:
    def __init__(self, Name):
        self.Name = Name
        
 
    def __len__(self):
        count = 0;
        for num in self.Name:
            count += 1
        return f"The number or letters are {count}"    

# without the __str__ it will show some hashid not give the complete details like output without __str__ is => <Main.Tester object at 0x0000019F896D2B50>

# __str__ method will give all the information of the class.
    def __str__(self):
        return f"The name name is {self.Name} str"    

# __repr__ method is also working same as __str__ but  in the absense of __str__ it will call the __repr__ method.
    def __repr__(self):
        return f"The name name is {self.Name} repr"  

# __call__ => This makes an object callable, just like a function, by defining the behavior of the call operator (`()`).
    def __call__(self):
        print("This is 73rd Day of Python Coding")      








