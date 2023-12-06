mat = [[1,2,3,4],
       [6,7,8,9],
       [10,11,12,13],
       [14,15,16,17]]
f = 0
s= int(input('enter the element to be search'))
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == s:
            print("element found at row:",i,"column:",j)
            f = 1
if f==0:
    print('element not found')
else:
    print("element found")