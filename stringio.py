# from io import StringIO

# buffer = StringIO()
# buffer.write("Hello")
# buffer.write(" Nila")
# buffer.write("!!")

# result = buffer.getvalue()
# print(result)

# buffer.close()



# text = "nila"
# if text == text[::-1]:   # Reverse string
#     print(text, "is a Palindrome")
# else:
#     print(text, "is not a Palindrome")

str1 = "apple"
str2 = "banana"

# Compare lexicographically
if str1 == str2:
    print("Strings are equal")
elif str1 < str2:
    print(f"{str1} comes before {str2}")
else:
    print(f"{str1} comes after {str2}")
