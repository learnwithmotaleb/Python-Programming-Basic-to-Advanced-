class Vehicle:
     def drive(self):
         print("Driving a vechicel")


class Car(Vehicle):
     def honk(self):
          print("Car is honking")


c = Car()
c.drive()
c.honk()