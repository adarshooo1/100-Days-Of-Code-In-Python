# Match Case statement simply matching the input and as per the defined input it is matching the case and print the values accounding to the input given by the User.
Day = int(input("Enter the Day:- "))

match Day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")            
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Enter the Correct format {Day}")

# In Java and C++ we also know that after matching a case all the below cases are also matched and print So,we use Break Statement but in Python no Break statement we use.
# Thats why python is easy and simple to learn.