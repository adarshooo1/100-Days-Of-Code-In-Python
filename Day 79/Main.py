class Mother:
    def __init__(self , Work):
        self.Work = Work

class Father:
    def __init__(self , Business):
        self.Business = Business

# In Python Multiple inheritance is easily supportable and convinient to use.
class Child(Mother , Father):
    def __init__(self ,work , Business , Study):
        Mother.__init__(self , work) #This will help to inherit the properties of the parent Msother class.
        Father.__init__(self , Business) #This will help to inherit the properties of the parent Father class.
        self.Study = Study

    def showChildDetail(self):
        print(f"Work = {self.Work}\nBusiness = {self.Business}\nStudy = {self.Study}")
        



Chld = Child("School Home Work","None","12th")
Chld.showChildDetail()

# This will the user that where we have to find the Mehtods and in which class.
print(Child.mro())
# Output: [<class '__main__.Child'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>]



