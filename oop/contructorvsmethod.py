
class Car:
     def __init__(self, name):
          self.name = name
          print(f"My name is {name}")

     def start(self):
          print(f"{self.name} is my Name")


car1 = Car("Abdul Motaleb")
car1.start()