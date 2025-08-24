num = int(input("Enter a some number: "))
sum_of_digits = 0

temp = num

while temp> 0:
     digit = temp % 10
     sum_of_digits = sum_of_digits + digit
     temp = temp // 10
print("Sum of digits: ",sum_of_digits)



