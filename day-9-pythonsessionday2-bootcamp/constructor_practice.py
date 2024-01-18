
# Constructor Practice:
# Create a class Person with a constructor that initializes name 
# and age attributes. Instantiate an object of this class and print its details.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

mydata = Person("Mewan Madhusha", 28)
print(f"Name: {mydata.name}, Age: {mydata.age}")

