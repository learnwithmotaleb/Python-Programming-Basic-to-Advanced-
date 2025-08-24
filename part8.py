name = "Motlaeb"
age = 20
print("My name is , of "+name)

print("Hello, Motaleb {} I am {} year old ".format(name, age))
print("Hello, Motaleb {0} I am {1} year old ".format(name, age))
print("Hello motlae{n} age{a}".format(n = name, a = age))


#interpulation in python c style
name = "Abdul Motaleb"
age = 22

print("My name is %s and i am %d years old" % (name, age))

#Specifier %s, %d, %f,%x,/%X , %o,%%, == String, Integer, Floating, Hexadecimal,Octal, Literal Percent

num = 123.4567
print("Default {}".format(num))
print("Round to 2 decimal {:.2f}".format(num))
print("Round to 3 decimal {:d}".format(25))
print(f"2 decimal : {num:.2f}")
print(f"Left aligned: {num:<10.2f}")   # '123.46    '
print(f"Binary: {25:b}")
print(f"Hex: {255:x}")   