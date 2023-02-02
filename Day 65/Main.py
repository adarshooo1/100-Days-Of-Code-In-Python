class MathsMethod:
    def __init__(self, num):
        self.num = num

    def addtwonum(self, n):
        self.num = self.num+n
        
    # Like this way we can declare the static method: 
    @staticmethod 
    def add(a,b):
        return(a + b)   


Eq1 = MathsMethod(20)
print(Eq1.num)


Eq1.addtwonum(5)
print(Eq1.num)

# We can call this method with the class name Very easily as well as static methods don't need objects or associate with the variable this is self dependent and the with the help of class name we can use this static funtion without making any other onject.
print(MathsMethod.add(10,12)) # With the class name we are able to access the method. 







