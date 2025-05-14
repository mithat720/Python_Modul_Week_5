class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Ad: {self.name}")
        print(f"Soyad: {self.surname}")
        print(f"TC Kimlik No: {self.tc_identification}")
        print(f"Telefon: {self.phone}")

class Account(Customer):  # Miras alındı
    def __init__(self, name, surname, tc_identification, phone, account_number, balance=0):
        super().__init__(name, surname, tc_identification, phone)  # Üst sınıfın (Customer) init'ini çağır
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL")
        else:
            print("Geçersiz tutar.")

    def money_check(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TL çekildi. Kalan bakiye: {self.balance} TL")
        else:
            print("Yetersiz bakiye. İşlem iptal edildi.")

    def display_balance(self):
        print(f"Mevcut Bakiye: {self.balance} TL")

# Hem müşteri hem hesap bilgileri aynı anda giriliyor
account1 = Account(
    name="Ahmet",
    surname="Yılmaz",
    tc_identification="12345678901",
    phone="0555 123 45 67",
    account_number="TR000100200300",
    balance=0
)

# Müşteri bilgilerini yazdır
print("MÜŞTERİ BİLGİLERİ")
account1.display_information()

# Banka işlemleri
print("\nBANKA İŞLEMLERİ")
account1.display_balance()
account1.deposit(1000)        # 1000 TL yatır
account1.money_check(400)     # 400 TL çek
account1.money_check(800)     # 800 TL çek (yetersiz)
account1.display_balance()    # Bakiye görüntüle