print("Decorators in Python!")

def hello():
    print("Hello World")

hello() # This will print hello world!

# Now see the work of Decorators.
# As you can see here we are making a function named Greet.
def Greet(gx): # Here Greet(gx) Greet is taking a function;
    def bfx(name): # Create another function in the greet;
        print("Hii!") # Print the function we want to print before the object.
        gx(name) # Call the function which we will pass in the another functions Arguement.
        print("How are you Today❤️")  # Print the function we want to print after the object.
    return bfx #Now we return the function.

@Greet #Annotation of Greet which will use, just above the function. In that we will call that arguement
def Name(name): # As we can see that the argument inside Name() function (name) was the same argument passed in the Greet(gx) and gx was calling the name function inside the function:- gx(name),Here Greet taking gx as argument and gx was taking the argument gx(name) 
    print(name)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Name("<Viewers>") # Here we called the function..
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@Greet
def Game(name):
    print(name)
Game("PUBG")  
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# #Example 2
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_hello():
#     print("Hello!")

# say_hello = my_decorator(say_hello)
# say_hello() #Example 1

# # With annotation
# @my_decorator
# def say_hello():
#     print("Hello 3")

# say_hello() #Example 2






 



