class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def Area(self ):
       return  self.width*self.height
    def Perimeter(self ):
       return 2*(self.width+self.height)
Rectangle1=Rectangle(5,7)
print(Rectangle1.Area())
print(Rectangle1.Perimeter())
    
