m=int(input("enter the number of rows"))
n=int(input("enter the number of columns"))
a=[]
for i in range(0,m):
    x=[]
    for j in range(0,n):
        x.append(int(input()))
    a.append(x)
for i in range(0,m):
    for j in range(0,n):
        print(a[i][j],end=" ")
    print()
p=int(input("enter the number of row2"))
q=int(input("enter the number of column2"))
b=[]
for i in range(0,p):
    x=[]
    for j in range(0,q):
        x.append(int(input()))
    b.append(x)
for i in range(0,p):
    for j in range(0,q):
        print(b[i][j],end=" ")
    print()
def sum_of_matrix(m,n,p,q,a,b):
    result=[]
    # Check if matrices have the same dimensions
    if m!= p or n!= q:
        print("Matrices must be of the same dimensions")

    result = []

    for i in range(len(a)):
        x = []
        for j in range(len(a[0])):
            # Add corresponding elements of matrix a and b
            x.append(a[i][j] + b[i][j])
        result.append(x)
    print(result)

menu=int(input("Enter the number of operation to be done : "))
if menu==1:
    sum_of_matrix(m,n,p,q,a,b)

def subtraction_of_matrix(m,n,p,q,a,b):
    result=[]
    # Check if matrices have the same dimensions
    if m!= p or n!= q:
        print("Matrices must be of the same dimensions")

    result = []

    for i in range(len(a)):
        x = []
        for j in range(len(a[0])):
            # subtract corresponding elements of matrix a and b
            x.append(a[i][j] - b[i][j])
        result.append(x)
    print(result)

if menu==2:
    subtraction_of_matrix(m,n,p,q,a,b)