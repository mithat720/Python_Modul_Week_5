# Create a "Customer" class and an "Account" class. Let the "Account" class inherit from the "Customer" class and represent a customer's bank account information.

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
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Name: {self.name}{self.surname}")
        print(f"TC ID: {self.tc_identification}")
        print(f"Phone: {self.phone}")

class Account(Customer):
    def __init__(self, customer, account_number, balance):
    # No need to inherit again, just store the customer object
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def money_check(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")   

customer1 = Customer("Sumeyra", " Turkcan", "19181635363", "31029384774")
account1 = Account(customer1, "192847490", 2500)

customer1.display_information()
account1.display_balance()
account1.deposit(700)
account1.money_check(1500)
account1.money_check(1800)

        