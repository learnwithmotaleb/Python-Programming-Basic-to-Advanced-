num = 1234567
reverse = 0
temp = num
while temp > 0:
     digit = temp % 10
     reverse = (reverse * 10)+ digit
     temp = temp // 10
print("Original Number: ",num)
print("Reverse of the number: ", reverse)