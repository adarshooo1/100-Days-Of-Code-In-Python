import random #Random is a built-in-module in Python which will help to grearate random number. 

print("Let's Play")

# This is showing the user that what to choose in the Input
print("0 :- Snake \n1 :- Water \n2 :- Gun")


while(True):
    # For taking the input from the user.
    UserInput = int(input("Choose a Input:- "))


    if UserInput < 0 or UserInput > 2:
         print("Invalid Input. Please select a correct input (0, 1, or 2)")
         continue


    # For Genrating the random number
    Computer_Input = random.randint(0,2)

    # Print User Input and Computer Input
    print(f"User input is {UserInput} and Computer input is {Computer_Input}")

    if(UserInput == 0 and Computer_Input == 1 or UserInput == 1 and Computer_Input == 2 or UserInput == 2 and Computer_Input == 0 ):
       print("You Win! Computer Loose")

    elif(UserInput == Computer_Input):
       print("Its a Tie!")

    else:
       print("You Loose! Computer Win")