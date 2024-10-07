l=[]
n=int(input("enter the value of n:"))
for i in range(n):
    x=int( input("enter the number:"))
    list.insert(l,i,x)
ch=0
while(ch!=3):
    print("\n1.ascending\n2.descending\n3.exit")
    ch=int(input("enter the choice:"))
    if(ch==1):
        for i in range(n):
            for j in range(i+1,n):
                if(l[i]>l[j]):
                   t=l[i]
                   l[i]=l[j]
                   l[j]=t
        print("the sorted list -ascending order:")
        for i in range(n):
            print(l[i],end=" ")
    elif(ch==2):
        for i in range (n):
            for j in range (i+1,n):
                if(l[i]<l[j]):
                   t=l[i]
                   l[i]=l[j]
                   l[j]=t
        print("the stored list-descending order:")
        for i in range(n):
            print(l[i],end=" ")
    elif(ch==3):
        print("thank you")
    else:
        print("enter a valid choice:")
