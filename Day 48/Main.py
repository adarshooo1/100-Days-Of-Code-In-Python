x = 5  # global variable

def example():
    global x  # modifies the global keyword and variable x
    x = 20 # Assigning the new value of the global variable.

example() #After printing this it will change the value of global variable onwards
print(x)    #Now x = 20



def example2():
    y = 100; #This is local variable which is only accessible in this function
    print(y)

example2()    #This is print the value of local variable.

# print(y) #This Y variable is not accessible outside this is function.


z = 400 #Global variable initialized
z = 500 #Global variable madified
print(z) #global value changed


def changed():
    z = 600
    print(z)# this is only changed inly inside this function




    