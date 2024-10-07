import os

os.system('cls')

p=float(input("enter the principal"))
n=int(input("enter the no of years"))
r=float(input("enter the rate of inperest"))
si=p*n*r/100
ci=p*(pow(1+r/100,n)-1)
print("simple intrest",si)
print("compound interest",ci)
