a = int(input())
b = int(input())
mat = []
for i in range(a):
    c = []
    for j in range(b):
        e = int(input('enter the element:'))
        c.append(e)
    print()
    mat.append(c)
for i in range(a):
    for j in range(b):
        print(mat[i][j],end=" ")
    print()