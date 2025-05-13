#Create a "Shape" class. Under this class, create two subclasses, the "Rectangle" and "Square" classes.
class Shape:
#- Let the "shape" class have two properties: "width" and "height."
    def __init__(self, width, height):
        self.width = width  
        self.height = height
#- Let the "Rectangle" class inherit from the "Shape" class and add an additional "calculate_area()" method.
class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height
#- Let the "Square" class inherit from the "Shape" class and calculate the area of ​​the square using the same "area_calculate()" method.
class Square(Shape):
    def calculate_area(self):
        return self.width * self.width  
#- Create a "Rectangle" and a "Square" instance, determine the width and height of each, and calculate the area of ​​each and print the results.
Rectangle1 = Rectangle(5, 10)
Square1 = Square(4, 4)
print("Rectangle Area:", Rectangle1.calculate_area())
print("Square Area:", Square1.calculate_area()) 

