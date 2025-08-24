num = 153
sum_of_cubes = 0
temp = num
n = len(str(num))
while temp > 0:
     digit = temp % 10
     sum_of_cubes = sum_of_cubes + digit **n
     temp = temp // 10
if num == sum_of_cubes:
    print(num, " is an Armstrong Number")
else:
     print(num, " is not an Armstrong Number")
    
   