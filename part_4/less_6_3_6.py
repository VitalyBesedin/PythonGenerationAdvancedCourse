n = int(input())
matrix = [tuple(input().split()) for _ in range(n)]

res = []
for i in range(n):
    if int(matrix[i][1]) == 4 or int(matrix[i][1]) == 5:
        res.append(matrix[i])

for i in range(n):
    print(*matrix[i])

print()
for i in range(len(res)):
    print(*res[i])
