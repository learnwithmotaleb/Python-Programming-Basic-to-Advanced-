class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

animals = [Dog(), Cat()]
for a in animals:
    a.sound()   # Object অনুযায়ী আলাদা sound()
