print("enter the no of rows and colums for matrix A")
r1=int(input("enter the no of rows"))
c1=int(input("enter the no of colums"))
A=[[0 for col in range(c1)] for row in range(r1)]
print("enter the value of A Matrix:")
for i in range(r1):
    for j in range(c1):
        x=int(input("enter a no"))
        A[i][j]=x
print("enter the no of rows and colums for matrix")
r2=int(input("enter a number of rows"))
c2=int(input("enter the number of colums"))
B=[[0 for col in range(c2)] for row in range(r2)]
print("enter the values of B matrix")
for i in range(r2):
    for j in range(c2):
        x=int(input("enter a number"))
        B[i][j]=x
if(r1==r2 and c1==c2):
    print("sum of matrix A and sum of Matrix")
    for i in range(r1):
        for j in range(c2):
            print(A[i][j]+B[i][j],end=" ")
        print()
else:
    print("matrix addition is not possible")
