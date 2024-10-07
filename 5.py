
num=int(input("enter number"))
wnum=num#working number stores num initially
rev=0
while(wnum>0):
    dig=wnum%10
    rev=rev*10+dig    
    wnum=wnum//10
if(num==rev):
    print("number",num,"palindrome!")
else:
    print("number",num,"not a palindrome!")
