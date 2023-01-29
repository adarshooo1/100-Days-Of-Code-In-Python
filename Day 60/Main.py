# Example 1:
class MyClass:

    def __init__(self , value):
        self._value = value

    def show(self):
        print(f"The value is:-{self._value}")    

val1 = MyClass(10) # Here we assign the value val1 = 10.
val1.show() #Output = 10

# Example 2:
# Getters Example

class GetterExample:
    def __init__(self,Value1):
        self.Value1 = Value1

    # Getter by calling this we will get the value.
    @property
    def ShowValue(self):
        return self.Value1


obj = GetterExample(100)
print(obj.ShowValue)

# Example 3:
# Getters and setters

class GetAndSet:
    def __init__(self, Value):
        self._value = Value

    @property #This is for setter.
    def Value(self):
        return self._value

    @Value.setter #This is for setter.
    def Value(self, aValue):
        self._value = aValue

    def printer(self):
        print(self._value)


obj2 = GetAndSet(500)
print(obj2.Value)
obj2.Value = 1000# Here we called the setter.
print(obj2.Value)#Like this way we call the properties of the Getter

obj2.printer()# This is normal printer funciton which will value.
        