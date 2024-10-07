prod=dict()
n=int(input("enter the no.of products"))
i=1
while(i<=n):
    pname=input("enter the products")
    pri=float(input("enter the price"))
    prod[pname]=pri
    i=i+1
ch=0
while ch!=5:
    print("\n1.append\n2.update\n3.delete\n4.display all\n5.exit")
    ch=int(input("enter your choice"))
    if(ch==1):
        pname=input("enter the new product name")
        pri=float(input("enter the price"))
        prod[pname]=pri
        print("\n\t product appended successfuly")
    elif(ch==2):
        upn=input("enter the product name to be update")
        if upn in prod:
            npr=float(input("enter the new price"))
            prod[upn]=npr
            print("\n\t product price update")
        else:
            print("product doen't exit")
    elif(ch==3):
        upn=input("enter the products name to be delete")
        if upn in prod:
            print(upn,end="")
            print(prod.pop(upn),end="")
            print("\t product does't exit")
        else:
            print("product does't exit")
    elif(ch==4):
        print("\n product name\t price")
        for i in prod:
            print(i,"\t",prod[i])
    elif(ch==5):
        print("thank you")
    else:
        print("enter a valid choice")
