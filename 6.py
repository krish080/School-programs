print("enter the number")
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
if(a>b):
    if(a>c):
        print(a,"is the greast of three numbers")
    else:
        print(c,"is the greast of three numbers")
else:    
    if(b>c):
        print(b,"is the greast of three numbers")
    else:
        print(c,"is the greast of three numbers")
