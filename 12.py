n=int(input("enter the no.of elements:"))
oned_list=[0 for size in range(n+1)]
print("Enter the input values:")
for size in range(n):
    x=int(input("enter the no:"))
    oned_list[size]=x
print()
print("user entered values:")
for size in range(n):
    print(oned_list[size],end =" ")
print()
e=int(input("enter the element to be inserted"))
x=int(input("enter the position to be inserted"))
for i in range(n):
    if(x-1==i):
        for j in range(n,i-1,-1):
            oned_list[j]=oned_list[j-1]
        oned_list[i]=e
        n=n+1
        break
print()
print("new array after insertion")
for size in range(n):
    print(oned_list[size],end=" ")
print()
x=int(input("enter the no.to be deleted:"))
for i in range(n):
    if(x==oned_list[i]):
        print(oned_list[i],"deleted")
        s=i
        for j in range(s,n-1):
            oned_list[j]=oned_list[j-i]
            n=n-1
print("list of elememts after deletion")
for size in range(n-1):
    print(oned_list[size])
