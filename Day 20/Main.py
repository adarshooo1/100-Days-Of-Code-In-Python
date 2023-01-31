# Function to get average of a number:
def Average(num1,num2):
    print(f"Average of {num1} and {num2} is:- ",int((num1+num2)/2))

Average(2,4)
Average(30.4,24.6)

# Function to get geometric Mean:
def GeometicMean(num1,num2):
    print(f"Geometric Mean of {num1} and {num2} is:-",int((num1*num2)/(num1+num2)))

GeometicMean(23,43)

# Function to get Maximum Number between 2 numbers
def MaxInNum (num1,num2):
    if num1 > num2:
        print(f"Maximum Number is:- {num1} & Minimum Number is:- {num2}")
    elif num1 == num2:
        print(f"Both are Equal {num1} & {num2}")
    else:
        print(f"Maximum Number is:- {num2} & Minimum Number is:- {num1}") 

MaxInNum(200,201)

# Function to get Lesser Number Between 2 number
def MinInNum (Num1,Num2):
    pass #If We don't want to complete this function so we can't leave this Otherwise
#           it will give error So,We can use pass to avoid the error

# Function to get Square
def square(x):
    return x**2

print(square(2))
print(square(3))  
print(square(4))  