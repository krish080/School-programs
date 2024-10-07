n=int(input("enter the no.of elements:"))
l=[]
for i in range (n):
    x=int(input("enter the elements:"))
    list.insert(l,i,x)
ch=0
while(ch!=4):
    print("\n1.max/n2.min\n3.exit")
    ch=int(input("enter your choice:"))
    if(ch==1):
        maxi=l[0]
        for i in range(1,n):
            if maxi < l[i]:
                maxi=l[i]
        print("the maximum elements in the list", maxi)
    elif(ch==2):
        mini=l[0]
        for i in range (1,n):
            if mini >l[i]:
                mini=l[i]
        print ("the minimum elements in the ",mini)
    elif (ch==3):
        print("thank you")
    else:
        print("enter a valid choice")
