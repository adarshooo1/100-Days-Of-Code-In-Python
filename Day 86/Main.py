a = True
print(a:=False) 


# Without walrus operator
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input == 'q':
        break
    else:
        number = int(user_input)
        if number > 10:
            print(f"{number} is greater than 10")


# # With walrus operator
while (user_input := input("Enter a number (or 'q' to quit): ")) != 'q':
    number = int(user_input)
    if number > 10:
        print(f"{number} is greater than 10")



# # Example 2:
list = [2,4,2,1,89]

while(n := len(list)) > 0:
    print(list.pop())

    
# #Example 3:

happy = True
print(happy:= True)


# Example 4:

# without walrus operator
Foods = list()

while True:
    Food = input("What food fo you like?: ")
    if Food == "quit":
        break
    Foods.append(Food)

print(list(Foods))    


# with walrus operator
Foods = list()
while(Food := input("What food do you like?: ")) != "quit":
    Foods.append(Food)

print(list(Foods)) 
