#  Question5: Create a "Customer" class and an "Account" class. Let the "Account" class inherit from the "Customer" class and represent a customer's bank account information.

# ##### Customer Class Features:
# - "name" (customer name)
# - "surname" (customer surname)
# - "tc_identification" (customer TR ID number)
# - "phone" (customer phone number)

# ##### Account Class Properties:
# - "customer" (a Customer object)
# - "account_number" (account number)
# - "balance" (account balance)

# ##### Customer Class Method:
# - "display_information()": Displays the customer's name, surname, TR ID number and telephone number.

# ##### Account Class Methods:
# - "deposit(self, amount)": A method that deposits a certain amount of money into the account.
# - "money_check(self, amount)": A method that withdraws a certain amount of money from the account. However, if there is not enough balance in the account, the transaction should not occur and a message should be displayed.
# - "display_balance()": A method that displays the account balance.

# Create these two classes, then create a Customer object and an Account object, add the customer information to the Account object, and perform account operations and view the results.
class Customer:
    def __init__(self, name, surname, tcID , phone):
        self.name = name
        self.surname = surname
        self.tcID = tcID
        self.phone = phone 
    def display_information(self):
        print(f"Name: {self.name}, Surname: {self.surname}, TC ID: {self.tcID}, Phone: {self.phone}")
class Account(Customer):
    def __init__(self, name, surname, tcID , phone, account_number, balance=0):
        super().__init__(name, surname, tcID , phone)
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount} TL")
    def money_check(self, amount):
        if amount > self.balance:
            print("Not enough balance!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount} TL")
    def display_balance(self):
        print(f"Account Balance: {self.balance} TL")    
# Create a Customer object
customer = Customer("Mehmet", "Altan", "12345678901", "0555-1234567")   
# Create an Account object
account = Account(customer.name, customer.surname, customer.tcID, customer.phone, "TR1234567890", 1000)
# Display customer information
print("Customer Information:")
customer.display_information()
# Display account information
print("\nAccount Information:") 
account.display_information()
account.display_balance()
# Perform account operations
print("\nPerforming Account Operations:")
account.deposit(500)    
account.display_balance()
account.money_check(200)
account.display_balance()
account.money_check(2000)  # Attempt to withdraw more than the balance
account.display_balance()
