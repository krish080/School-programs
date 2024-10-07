rn =int(input("enter the no.of rows"))
cn=int(input("enter the no.of coloumns"))
A=[[0 for col in range (cn)] for row in range (rn)]
for i in range (rn):
    for j in range(cn):
            x=int(input("enter the no"))
            A[i] [j]=x
print("the given matrix is")
for i in range (rn):
    for j in range (cn):
        print(A[i][j], end=" ")
    print(" ")
print("\n.upper half elements")
for row in range (rn):
    for col in range (cn):
        if  (row <=col):
            print(A[row] [col], end= " ")
        else:
            print (end= " ")
    print (" ")
print ("\n diagonal elements ")
for i in range (rn):
    for j in range (cn):
            if(i==j or i+j==rn-1):
                    print (A [i]  [j],end= " ")
            else:
                    print (end= " ")
    print(" ")
print ("\n coloumn elements:")
for i in range (rn):
        for j in range (cn):
                print (A [i] [j] , end ="\t")
        print (" ")
cols=[0 for col in range (cn)]
for i in range (cn):
        for j in range (rn):
            cols[i]+=A[j] [i]
print("_________________")
for i in range(cn):
    print(cols[i], end="\t")
print()
print("_________________")
