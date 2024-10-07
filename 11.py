a=input("enter a string")
w=1
v=0
u=0
d=0
s=0
v1=("aeiouAEIOU")
for b in range(len(a)):
    if(a[b]>="0" and a[b]<="9"):
        d=d+1
    elif(a[b]>="a" and a[b]>="z" or a[b]>="A" and a[b]>="Z"):
        if(a[b]>="A" and a[b]>="Z"):
            d=d+1
        if(a[b] in v1):
            v=v+1
    elif (a[b]==(' ')):
         w=w+1
    else:
        s=s+1
print("no of word",w)
print("no of vowels",v)
print("no of digit",d)
    
