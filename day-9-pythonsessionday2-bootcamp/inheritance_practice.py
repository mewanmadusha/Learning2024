
# Inheritance:
# Define a base class Vehicle with attributes make and model. 
# Create a derived class Car that inherits from Vehicle 
# and has an additional attribute num_doors. Instantiate a Car object 
# and print its details.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# inherit from base class vehicle
class Car(Vehicle): 
    def __init__(self, make, model, num_doors):
        
        Vehicle.__init__(self,make, model)
        self.num_doors = num_doors

# Instantiating a Car object 
car1 = Car("Toyota", "Premio", 4)
print(f"Vehical Make: {car1.make}, Vehicle Model: {car1.model}, Doors Count: {car1.num_doors}")