a = int(input())
b = int(input())
mat = []
d={}
for i in range(a):
    c=[]
    for j in range(b):
        e = int(input('element:'))
        c.append(e)
    print()
    mat.append(c)
for i in range(a):
    res = 0
    for j in range(b):
        res=res*10+mat[i][j]
    d[i]=res
print(d)
l=[]
for i,j in d.items():
    if j not in l:
        l.append(j)
    else:
        print('duplicate found')

