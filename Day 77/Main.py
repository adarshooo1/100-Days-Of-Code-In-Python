class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        # return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k" #Case 1 , This will retun the output as a class string
        return Vector(self.i + x.i ,  self.j + x.j ,  self.k + x.k) #Case 2 , This will return the  output as a Main Class Vector Because we are passing a class as a constructor.



V1 = Vector(3,5,6)       
print(V1) 

V2 = Vector(9,10,11)
print(V2)

print(V1 + V2)

print(type(V1 + V2)) # Output is <class 'str'> or <class '__main__.Vector'> : as per Case:1 and Case:2
