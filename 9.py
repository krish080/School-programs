ch=0
while(ch!=3):
        print("\n1 .pyramid \n2 . inverted hollow pyramid \n3.exit")
        ch=int(input("enter your choice:"))
        if(ch==1):
            n=int(input("enter the number of steps:"))
            
            for i in range (0,n+1):
                for k in range(i,n+2):
                    print(end="  ")
                
                for j in range(2*i+1):
                    
                    print("*",end=" ")
                print( )
                
        elif(ch==2):
            n=int(input("enter the number of steps:"))
            for i in range (n,0,-1):
                for j in range (n-i):
                    print(' ',end=" ")
                    
                for j in range (2*i-1):
                    if(i==0 or j==2*i-2 or i==n or j==0):
                        print("*",end=" ")
                    else:
                        print(' ',end=" ")
                print( )
        elif(ch==3):
            print("thank you")
        else:
            print("enter a valid option")
