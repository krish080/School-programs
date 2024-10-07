ch=0
while(ch!=3):
    print("\n 1.horizontal\n 2.alphabet(right to left)\n 3.exit")
    ch=int(input("enter your choice"))
    if(ch==1):
        n=int(input("enter the number of stages(1-9):"))
        for i in range(1,n+1):
            for j in range (i,n+1):
                print(i,end=" ")
            print()    
    elif(ch==2):
            n=int(input("enter the number of rows:"))
            for i in range(n):
                c=65
                for k in range(i,n-1):
                    print(end=" ")
                for j in range(i+1):
                    print(chr(c),end=" ")
                    c=c+1
                print()
    elif(ch==3):
           print("thank you")
    else:
        print("enter a valid choice")
