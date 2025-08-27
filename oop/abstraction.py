from abc import ABC, abstractmethod

class Shape(ABC):
     @abstractmethod
     def area(self):
          pass

class Circle(Shape):
     def __init__(self, r):
          self.r = r 

     def area(self):
          return 3.14*self.r * self.r

class Square(Shape):
     def __init__(self, s):
          self.s = s
     
     def area(self):
          return self.s * self.s
     
shapes = [ Circle(5), Square(4)]

for s in shapes:
     print(s.area())