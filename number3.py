num = int(input("Enter some number Check Palindrome: "))
reverse = 0
temp = num
while temp> 0:
     digit = temp % 10
     reverse = reverse * 10 +digit
     temp = temp // 10
if num == reverse:
     print(num , " is a palindrome")
else:
     print(num, " is not a palindrome")