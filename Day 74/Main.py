class shape:
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def area(self) :
        return self.x * self.y

numb = shape(3,5)
print(numb.area())


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
        # Here in Super class it was asking for the input x and y but, here in this case , we have called the radius 2 times. as x and y
        super().__init__(radius, radius)


    def area(self):
        # This will call the super class which is (class shape) area method.
        return 3.14*super().area() 


numb2 = Circle(12)
print(numb2.area())


