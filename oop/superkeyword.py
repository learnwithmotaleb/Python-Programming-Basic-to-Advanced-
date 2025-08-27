class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent init called")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # Parent এর init call
        self.age = age
        print("Child init called")

c = Child("Rahim", 20)


class A:
    def show(self):
        print("A class show()")

class B(A):
    def show(self):
        super().show()   # Parent এর method call
        print("B class show()")

b = B()
b.show()
