class BankAccount:
     def __init__(self, balance):
          self.__m = balance
     def deposit(self, amount):
          self.__m += amount
     def get_balance(self):
          return self.__m

acc = BankAccount(5000)
acc.deposit(400)
print(acc.get_balance())