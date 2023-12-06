mat = [[1,2,3],[4,5,6],[7,8,9]]
l=[]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if i<j:
            l.append(mat[i][j])
k=0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if i>j:
            mat[i][j]=l[k]
            k+=1
for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j],end=" ")
    print()
