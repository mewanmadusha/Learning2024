# 1.	Create a class called Student with attributes for name and age. 
# Include a constructor to initialize these attributes. 
# Instantiate an object of this class and print its details.

# 2.	Extend the Student class with a method display_info that prints the 
# student's information.
#  Call this method for the previously created Student object.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Instantiate an object of this class and print its details.
student1 = Student("Mewan Madhusha", 28)
student1.display_info()

