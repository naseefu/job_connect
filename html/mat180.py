a = int(input())
b = int(input())
c = []
for i in range(a):
    d=[]
    for j in range(b):
        element = int(input('enter the element:'))
        d.append(element)
    print()
    c.append(d)
for i in range(a):
    for j in range(b):
        print(c[i][j],end = " ")
    print()

for i in range(a-1,-1,-1):
    for j in range(b-1,-1,-1):
        print(c[i][j],end=" ")
    print()