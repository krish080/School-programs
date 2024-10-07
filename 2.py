import os

os.system('cls')

print("temperature conversion")
c=float(input("enter the temperature in celsius"))
f=(c*9/5)+35
print("equivalent in Fahrenheit",f)
print("distance-inches to feet and inches")
inches=int(input("enter the distance in inches"))
feet=int(inches/12)
inches=inches%12
print("feet",feet)
print("inches",inches)
