s3=" "
s4=" "
ch=0
while(ch!=6):
    print("\n 1.length\n 2.copy \n 3.concatenate \n 4.reverse \n 5.compare \n 6.exit")
    ch=int(input("enter your choice"))
    if(ch==1):
        s1=input("enter a string")
        leng=-1
        for i in s1:
            leng+=1
        print("the length of the string is:",leng)
    elif(ch==2):
        s1=input("enter a string")
        for i in s1:
            s3+=i
        print("copied string is:",s3)
    elif(ch==3):
          s1= input("enter a string")
          s2= input("enter a string")
          for i in s2:
              s1+=i
          print("the concatenated string is:",s1)
    elif(ch==4):
        s1=input("enter a string")
        leng=len(s1)
        for a in range(-1,(-leng)-1,-1):
            print("the reversed  string is:",s1[a])
    elif(ch==5):
        flag=0
        s1=input("enter a string")
        s2=input("enter a string")
        len1=0
        for i in s1:
            len1+=1
        len2=0
        for i in s2:
            len2+=1
        if(len1==len2):
            for i in range(len1):
                if(s1[i]!=s2[i]):
                    flag=1
                    break
        else:
            flag=1
        if(flag==0):
            print("string are equal")
        else:
            print("string are not equal")
    elif(ch==6):
        print("thank you")
    else:
        print("enter a valid choice")
