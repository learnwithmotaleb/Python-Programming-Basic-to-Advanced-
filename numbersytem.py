# a = 10

# print(a)
# print("Binary Print")
# print(bin(a))
# print("Octal Print")

# print(oct(a))
# print("Hexadecimal Print")

# print(hex(a))
# print("Integer Print")

# print(int("1010"))


decimal = 255

binary = bin(decimal)    # '0b11111111'
octal = oct(decimal)     # '0o377'
hexa = hex(decimal)  

print(binary)    # '0xff'
print(octal)    # '0xff'
print(hexa)    # '0xff'

# Reverse Conversion
print(int('11111111', 2))  # Binary → Decimal 255
print(int('377', 8))       # Octal → Decimal 255
print(int('ff', 16))       # Hex → Decimal 255

