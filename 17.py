tup1=eval(input("enter few over score:"))
ch=0
while(ch!=6):
    print("\n1.length of the tuple\n2.slicing\n3.concantenation\n4.membership operator\n5.count\n6.exit")
    ch=int(input("enter your choice"))
    if(ch==1):
        print("no.of over:",len(tup1))
    elif(ch==2):
        print("enter the starting and the ending over:")
        s,e=int(input()),int(input())
        print("slicing of score card:")
        print(tup1[s:e])
    elif(ch==3):
        tup2=eval(input("enter few more over score:"))
        tup1=tup1+tup2
        print("new score card:",tup1)
    elif(ch==4):
        print("Membership operaator")
        print("Enter no to be searched")
        x=int(input("enter the runs to be searched:"))
        if x in tup1:
            print("runs present in the over:",tup1.index(x))
        else:
            print("runs not present in the scorecard")
        print("\n NOT IN operator")
        print("runs in the scorecard:",tup1)
        x=int(input("enter the runs to be searched:"))
        if x not in tup1:
            print("runs not present in the scorecard")
        else:
            print("runs present in the over",tup1.index(x)+1)
    elif(ch==5):
        print("elements in tup1:",tup1)
        x=int(input("enter the runs:"))
        print(x,"runs present in the scorecard",tup1.count(x),"times(s)")
    elif(ch==6):
        print("thank you")                          

