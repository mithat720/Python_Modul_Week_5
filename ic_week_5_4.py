class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Marka: {self.make}")
        print(f"Model: {self.model}")
        print(f"Yıl: {self.year}")

class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)  # Üst sınıfın kurucusu çağrılıyor
        self.four_wheel_drive = four_wheel_drive

    def display_info(self):
        super().display_info()  # Üst sınıfın bilgilerini yazdır
        print(f"Dört Çeker: {'Evet' if self.four_wheel_drive else 'Hayır'}")

class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f"Maksimum Hız: {self.max_speed} km/s")


# Off-Road Aracı
suv = OffRoadVehicle("Toyota", "Land Cruiser", 2022, True)

# Spor Araba
sport_car = SportsCar("Ferrari", "488 GTB", 2020, 330)

# Bilgileri Yazdır
print("Arazi Aracı Bilgileri:")
suv.display_info()

print("\nSpor Araba Bilgileri:")
sport_car.display_info()
