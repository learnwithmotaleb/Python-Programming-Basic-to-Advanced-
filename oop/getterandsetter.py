class Person:

     def __init__(self, name):
          self.__name__ = name
     
     @property
     def name(self):
          return self.__name__

     @name.setter
     def name(self, new_name):
          if len(new_name)>2:
               self.__name__ = new_name

          else:
               print("Name to short!")



p = Person("Motaleb")
print(p.name)
p.name = "Ab"
p.name = "Sonia Akter"
print(p.name)