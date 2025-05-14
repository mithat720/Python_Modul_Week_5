# ##
# Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:

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

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
 
class OffRoadVehicle(Vehicle):
    def __init__(self, four_wheel_drive, make, model, year):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self, max_speed, make, model, year):
        super().__init__(make, model, year)
        self.max_speed = max_speed
   
suv = OffRoadVehicle(True, "Toyota", "Land Cruiser", 2020)
sportCar = SportsCar("200", "Ferrari", "488", 2021)

print("Off-Road Vehicle:")
suv.display_info()
print("Four Wheel Drive:", suv.four_wheel_drive)

print("\nSports Car:")  
sportCar.display_info()
print("Max Speed:", sportCar.max_speed)

