class Person:

# __init__ is a constructor.

    def __init__(self,Player,Game): # This is a parameterised constructor
        self.Player = Player
        self.Game = Game
        

    def info(self): # This is a Default Constructor, In which we have passed the self keyword which will dynamically allocate the memory at the runtime, And call the objects associated with self. 
        print(f"{self.Player} is a {self.Game} player")   
    


H1 = Person("Sachin Tendulkar" , "Cricket") # We Create a template like this, and now we can make as many objects like that.
H1.info() # A function which will print Objects.
# If we want to call the onjects then we have to pass the name to print:
print(H1.Player)
print(H1.Game)


        