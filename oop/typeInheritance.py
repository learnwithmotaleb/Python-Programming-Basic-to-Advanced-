# Inheritance , Single inheritance, multilevel inhritance
# hierarchical inheritance, multiple inheritance


# single Inheritance
# class A:
#      def show(self):print("A Class")

# class B(A):
#      pass


# b = B()
# b.show()

# Multileve in
# class A: 
#      def show(self):
#           print("Hello Class A")
# class B(A): pass
# class C(B):pass


# c = C()
# c.show()

# Hierarchical Inheritance
# class A:
#      def show(self):
#           print("hello class A")

# class B(A):pass
# class C(A):pass

# c = C()
# c.show()


# Multiple Inheritance

class A:
     def show(self):
          print("Hello, Class A")


class B: 
     def show2(self):
          print("Hello, Class B")

class C(A, B):
     pass

c = C()
c.show()
c.show2()