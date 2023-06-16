l  = input().split()
n, m = int(l[0]), int(l[1])
list = [i for i in range(1,m+1)]

matrix = []
for i in range(n):
    matrix.append(list)
    list = list[1:] + list[:1]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

