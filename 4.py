num=int(input("enter a three digit number:"))
summ=0
temp=num
while(temp>0):
    digit=temp%10
    
    summ+=digit**3
    
    temp//=10

    print(temp)
if(num==summ):
  print(num,"it is an amstrong number")
else:
  print(num,"is not an amstrong number")     
