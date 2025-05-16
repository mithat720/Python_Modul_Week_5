# Create a "Vehicle" class in Python. Make sure this class has the following properties:

# ##### Features:
# - "make" (Brand of vehicle)
# - "model" (Vehicle model)
# - "year" (Year of manufacture of the vehicle)

# Create a "Vehicle" class and create two derived subclasses, "Off-Road Vehicle" (SUV) and "SportsCar" classes.

# - The "Off-Road Vehicle" class inherits from the "Vehicle" class and adds an additional "four_wheel drive" feature.
# - Let the "SportCar" class inherit from the "Vehicle" class and add a "max_speed" property.

# Create an instance of each class, determine its properties, and write a program to display these properties.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)  #call parent constructor
        self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

suv = OffRoadVehicle("Toyota", "Land Cruiser", 2022, True)
sports_car = SportsCar("Ferrari", "488", 2019, 330)

print(f"SUV: {suv.make}, {suv.model}, 4WD: {suv.four_wheel_drive}")
print(f"Sports Car: {sports_car.make}, {sports_car.model}, Max speed: {sports_car.max_speed} km/h")