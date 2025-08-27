class Parent:
     def __init__(self):
          self._protected = "Protected"
          self.__private = "Private"

class Child(Parent):
     def show(self):
          print("Protected ", self._protected)


c = Child()
c.show()