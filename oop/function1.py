# function
def functionName ():
     print("Hello Function")


functionName()

def HelloWorld():
     return "I Love Love"


print(HelloWorld())

def add(a,b):
     return a + b

def sub(a, b):
     return a-b

def square(x):
     return x*x



print(add(44, 6))
print(sub(55, 44))
print(square(5))

def introduce(name, age = 22):
     print(f"My Name is {name}, I am {age} year old")



introduce("Abdul Motaleb")
introduce("Nila Akter", 20)


def squareF(x):
     return x * x
result = squareF(6)
print(result)


squareL = lambda x: x*x
print(squareL(5))

sum = lambda x, y: x + y
print(sum(4,5))