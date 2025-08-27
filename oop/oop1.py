class Person:
     def __init__(self, name, age):
          self.name = name 
          self.age = age


# Object
p1 =  Person("Abdul Motaleb",22)
print(p1.name,p1.age)


class Car:
     def __init__(self, brand, model):
          self.brand = brand
          self.model = model
     def start(self):
          print(f"{self.brand} {self.model} is starting....")

car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")

car1.start()
car2.start()