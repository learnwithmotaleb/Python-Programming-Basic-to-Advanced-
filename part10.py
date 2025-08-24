import math
#Arithmetic Operator +,-,*,/,%,//,**
#Assignment Operator =, +=, -=, *=,/=,%=,//=, **=,
#Compersion Operator ==, !=, >, <, >=, <=
#Logical Operator and, or, not,
#Membership Operator in, not in,
#Identity Operator is , is not
#Bitwise Operator &, |,^,~,<<, >>


#Now we wll make a program to show all the oprator Area of Traiangle and Circle

#formula of area of traiangle  = 1/2 *base*height
#formula of area of circle = pi*r*r

base = float(input("Enter the base of traiangle: "))
height = float(input("Enter the height of traiangle: "))
area_of_traiangle = 0.5 *base*height
print("The area of traiangle is: ",area_of_traiangle)





radius = float(input("Enter radius of circle: "))
area_circle = math.pi * radius **2
print("Area of Circle:", area_circle)
