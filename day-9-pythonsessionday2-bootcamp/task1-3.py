# Create a base class Animal with an attribute species.
#  Derive a class Dog from Animal with an additional attribute breed. Instantiate a Dog 
# object and print its species and breed.

class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, species, breed):
        # Call the __init__ method of the base class (Animal)
        Animal.__init__(self,species)
        self.breed = breed

# Instantiating a Dog object and print its species and breed.
dog1 = Dog("Shibuu", "Japanese Spitz")
print(f"Dog Species: {dog1.species}, Breed: {dog1.breed}")
