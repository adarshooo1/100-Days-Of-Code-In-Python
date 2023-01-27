class person: # This is class.
    #This is user defined Objects because this is created by us.
    name = "Adarsh" # This is a Default object of this class.(This is Object)
    occupation = "Software Developer" # This is a Default object of this class.(This is Object)

    # function with a Keyword:- self
    def info(self):# Self is a keyword which is Dynamically assigning the value at the run time.
        self.name
        self.occupation
        print(f"{self.name} is a {self.occupation}")

    # def __init__(self,name, occupation):# Self is a keyword which is Dynamically assigning the value at the run time.
    #     self.name = name
    #     self.occupation = occupation
    #     print(f"{self.name} is a {self.occupation}")


# Ex1
H1 = person()
print(H1.name ,",", H1.occupation)

# Ex2
H2 = person()
H2.name = "Deepanshu" # Here we are assigning the new value of the object because the class objects value is Default.
H2.occupation = "Shopkeeper" # Here we are assigning the new value of the object because the class objects value is Default.
H2.info()

# Ex3
H2.name = "Madan"
H2.info() # If we have already passed the value of a variable outside the function and we again pass the value then it will re-assign the value of the Object.
print(H2.name)



class Person2():
    def __init__(self,Name,Occupation):
        self.Name = Name
        self.Occupation = Occupation

    def info(self):
        print(f"Mr. {self.Name} is a {self.Occupation}")    


H3 = Person2("Narendra Modi","Prime Minister")
H3.info()

