# CALCULATOR
print("CALCULATOR")
num1 = int(input("Enter num1:- "))
num2 = int(input("Enter num2:- "))

print("////////////////////////////////")
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponential\n7.Floor Division")
print("////////////////////////////////")

operation = int(input("Choose a option for Calculation :- "))
if(operation == 1):
   print("your answer is:- ",num1+num2)
elif(operation == 2):
    print("your answer is:- ",num1-num2)
elif(operation == 3):
    print("your answer is:- ",num1*num2)  
elif(operation == 4):
    print("your answer is:- ",num1/num2)
elif(operation == 5):
    print("your answer is:- ",num1%num2)  
elif(operation == 6):
    print("your answer is:- ",num1**num2)
elif(operation == 7):
    print("your answer is:- ",num1//num2)        
else:
    print("Wrong Option Choosen")   







