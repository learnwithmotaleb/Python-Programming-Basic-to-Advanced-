# n = 10
# a, b = 0, 1
# # print("Fibonacci Series: ")
# for i in range(n):
#      print(a , end= ' ')
#      a, b = b, a+b



     # def fibonacci(n):
     #      if(stopping_condition):
     #           return Value
     #      else:
     #           return fibonacci(smaller_problem)

def factorial(n):
     if n == 1:
          return 1
     else: return n * factorial(n-1)

print(factorial(5))