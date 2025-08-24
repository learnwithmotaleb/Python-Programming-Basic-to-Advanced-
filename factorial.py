# n = 5
# fact = 1
# for i in range(1, n+1):
#      fact = fact * i
#      print(fact)


# for table in range(2, 6):          # Outer Loop (টেবিল নাম্বার)
#     print(f"\nMultiplication Table of {table}")
#     for i in range(1, 11):         # Inner Loop (গুণ করার সংখ্যা)
#         print(f"{table} x {i} = {table*i}")


for table in range(2, 11):
     print(f"\nMultiplication Table of {table}")
     for i in range(1, 11):
          print(f"{table} x {i} = {table*i}")