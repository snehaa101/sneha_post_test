# CREATE A CLASS "bankaccount"
class BankAccount:
    def __init__(self):
        # private variable
        self.__balance = 1000

    def deposite(self, amount):
        self.__balance += amount
        print(f"deposited{amount}. New balance : {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("insufficient..!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        print(f"Current balance: {self.__balance}")


print(" Account 1 Operations :")
account1 = BankAccount()
account1.get_balance()
account1.deposit(5000)
account1.withdraw(3000)
account1.withdraw(20000)  # Tests insufficient funds condition

print("\n Account 2 Operations :")
account2 = BankAccount()
account2.get_balance()
account2.deposit(12000)
account2.withdraw(8000)
