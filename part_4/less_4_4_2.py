# put your python code here
n, m = int(input()), int(input())
matrix = []

for i in range(n):
    elem = [input() for j in range(m)]
    matrix.append(elem)


for c in range(n):
    for r in range(m):
        print(matrix[c][r], end=' ')
    print()

print()
for c in range(m):
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()

