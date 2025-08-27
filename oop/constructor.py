class BankAccount:
     def __init__(self, account_number,balance =0):
          self.account_number = account_number
          self.balance = balance
     
     def deposit(self, amount):
          self.balance = self.balance + amount
          print(f"Deposited {amount}, New Balance = {self.balance}")

     def Withdraw(self, amount):
          if amount <= self.balance:
               self.balance -= amount
               print(f"Withdraw {amount}, New Balance = {self.balance}")


          else:
               print("Insufficient Balance!")

# object
acc1 = BankAccount("ABC123", 500)
acc1.deposit(200)
acc1.Withdraw(100)

