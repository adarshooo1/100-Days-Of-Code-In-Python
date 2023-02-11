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
        super().__init__(radius, radius)


    def area(self):
        return 3.14*super().area() 


numb2 = Circle(12)
print(numb2.area())


