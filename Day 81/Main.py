# Base class
class A:
    pass

# Derived class
class B(A):
    pass


# Real World Example of Hybrid Inheritance.:
class Car:
    def __init__(self,Brand,Name,Model):
        self.Brand = Brand
        self.Name = Name
        self.Model = Model

    def ShowCarDetail(self):
        print(f"This is {self.Brand} Car Named - {self.Name} and Modle Number is {self.Model}")    


class PertolCar(Car):
    def __init__(self , Brand , Name , Model , FuelCapacity):
        #Here We can call Parent Name as well as Super() to show to associativity of the argument of the praent class
        Car.__init__(self , Brand , Name , Model)
        self.FuelCapacity = FuelCapacity

    def ShowCarDetail(self):
        print(f"This is {self.Brand} Car Named - {self.Name} {self.Model} and the Fuel Capacity is {self.FuelCapacity}")    


class CNG(Car):
    def __init__(self, Brand , Name , Model , CngTankCapacity):
        Car.__init__(Brand , Name , Model)
        self.CngTankCapacity = CngTankCapacity

class ElectricCar(Car):
    def __init__(self, Brand , Name , Model , BattryPowerCapacity):
        #Here We can call Parent Name as well as Super() to show to associativity of the argument of the praent class
        super().__init__(Brand , Name , Model)
        self.BattryPowerCapacity = BattryPowerCapacity

    def ShowCarDetail(self):
        print(f"This is {self.Brand} Car Named - {self.Name} {self.Model} and the Battry Capacity is {self.BattryPowerCapacity}")  

# Here With this we can achieve Hybrid Inheritance
class HybridCar(PertolCar, ElectricCar):
    def __init__(self, Brand, Name, Model, FuelCapacity, BattryPowerCapacity):
        PertolCar.__init__(self, Brand, Name, Model, FuelCapacity)
        ElectricCar.__init__(self, Brand, Name, Model, BattryPowerCapacity)

    def ShowCarDetail(self):
        print(f"This is a Hybrid car Name :- {self.Brand} {self.Name} {self.Model} and Fuel Capacity of {self.FuelCapacity} and Battery Capacity of {self.BattryPowerCapacity}")      


Car1 = PertolCar("Ford", "Mustang" , "M1" , "30 Liters")
Car1.ShowCarDetail()

Car2 = ElectricCar("Tesla", "Vision" , "T1" , "Litium-ion Battry 25000 mAh")
Car2.ShowCarDetail()

car3 = HybridCar("McLaren", "SpeedTa!l", "P1", "15 Liters", "15000 mAh")
car3.ShowCarDetail()



# Example of Hierarchical Inheritance:
class Vehicle(Car):
    def __init__(self, Brand, Name, Model, Wheels):
        Car.__init__(self, Brand, Name, Model)
        self.Wheels = Wheels

    def ShowVehicleDetail(self):
        print(f"This is a {self.Brand} {self.Name} {self.Model} with {self.Wheels} wheels")

class Bike(Vehicle):
    def __init__(self, Brand, Name, Model, Wheels, HandleType):
        Vehicle.__init__(self, Brand, Name, Model, Wheels)
        self.HandleType = HandleType

    def ShowBikeDetail(self):
        print(f"This is a {self.Brand} {self.Name} {self.Model} bike with {self.Wheels} wheels and {self.HandleType} handle")

class Car2(Vehicle):
    def __init__(self, Brand, Name, Model, Wheels, SeatingCapacity):
        Vehicle.__init__(self, Brand, Name, Model, Wheels)
        self.SeatingCapacity = SeatingCapacity

    def ShowCar2Detail(self):
        print(f"This is a {self.Brand} {self.Name} {self.Model} car with {self.Wheels} wheels and {self.SeatingCapacity} seating capacity")


bike = Bike("Harley Davidson", "Sportster", "XL883N", 2, "Drag")
bike.ShowVehicleDetail()
bike.ShowBikeDetail()

car2 = Car2("Toyota", "Corolla", "Gli", 4, 5)
car2.ShowVehicleDetail()
car2.ShowCar2Detail()


