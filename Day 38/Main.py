# Example 1.
Inp = input("Enter any value between 5 to 9:- ")
if(int(Inp) < 5 or int(Inp) > 9):#It is a type of custom error
    raise ValueError("Value should be Between 5 and 9") #IF error in program is based on Input Integer based;
    # Aloh with it does't need to write this in conditional format whenever we want to raise a specific type of error just wirte this keyword and show the error.

# Example 2.
Salary = int(input("Enter your Salary in Amount:-"))
if(2000 > Salary > 10000):
    raise ValueError("Salary not Justified")#Like Here we are throwing error if the salary of the User is under
                                            #the range than its ok else it will throw the exception error
else:
    if(Salary > 2000):
        Salary += 2000
    print(f"Your Salary is:-{Salary}")

#Like this way we can make raise error for guiding the user that not cross the limits and Exceptions are Helping in that
#by which get error till the user not enterd the Corred Information of the given Data.