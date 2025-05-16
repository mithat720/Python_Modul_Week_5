
# Create a "Shape" class. Under this class, create two subclasses, the "Rectangle" and "Square" classes.

# - Let the "shape" class have two properties: "width" and "height."
# - Let the "Rectangle" class inherit from the "Shape" class and add an additional "calculate_area()" method.
# - Let the "Square" class inherit from the "Shape" class and calculate the area of ​​the square using the same "area_calculate()" method.
# - Create a "Rectangle" and a "Square" instance, determine the width and height of each, and calculate the area of ​​each and print the results.

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def calculate_area(self):
         return self.width * self.height
    
class Square(Shape):
    def calculate_area(self):
         return self.width * self.height  #for square width == height
    
my_rectangle = Rectangle(7,10)
my_square = Square(8,8)

print("Rectangle Area:", my_rectangle.calculate_area())
print("Square Area:", my_square.calculate_area())


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height
    
    def display_information(self):
        print("Shape: Rectangle")
        print(f"Width: {self.width}, Height: {self.height}")
        print(f"Area: {self.calculate_area()}")
        print()

class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def calculate_area(self):
        return self.side * self.side  

    def display_information(self):
        print("Shape: Square")
        print(f"Side: {self.side}")
        print(f"Area: {self.calculate_area()}")
        print()

my_rectangle = Rectangle(7, 10)
my_square = Square(8)

my_rectangle.display_information()
my_square.display_information()