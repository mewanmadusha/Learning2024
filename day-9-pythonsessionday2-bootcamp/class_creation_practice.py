# Class Creation:
# Write a Python class named Rectangle with attributes width and height.
#  Include a method that calculates and returns the area of the rectangle.


class Rectangle:

    def calculate_area(self,width,height):
        return width * height

rectangle1 = Rectangle()
area = rectangle1.calculate_area(10,20)
print(f"Area: {area}")