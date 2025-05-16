# Temel şekil sınıfı
class shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class rectangle(shape):
    def calculate_area_rectangle(self):
        return self.width * self.height

class square(shape):
    def __init__(self, side):
        super().__init__(side, side)    
    
    def calculate_area_square(self):
        return self.width * self.height
    
k = square(5)
print(k.calculate_area_square())

d = rectangle(5, 10)
print(d.calculate_area_rectangle())