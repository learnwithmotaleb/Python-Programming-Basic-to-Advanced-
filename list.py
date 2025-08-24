numbers = [10,30,40,55,77]
total = sum(numbers)
avarage = total/len(numbers)

print("All Number: ",numbers)
print("Total: ",total)
print("Avarage: ", avarage)
print("Max: ",max(numbers))
print("Min: ",min(numbers))



print("All Number:", end=" ")
for num in numbers:     # for-each loop
    print(num, end=" ")
