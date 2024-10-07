units=int(input("enter the units consumed"))
if(units<=50):
    amt=0.0
elif(units>=51 and units<=100):
    amt=units*0.60
elif(units>=101 and units<=200):
    amt=units*0.75
elif(units>=201 and units<=300):
     amt=units*0.90
else:
    amt=units*1.15
print("for the",units,"units you have to pay:",amt)
