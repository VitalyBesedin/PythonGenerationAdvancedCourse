n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
upper, lower, left, right = 0, 0, 0, 0

for i in range(n):
    upper += sum(matrix[i][i+1:n-i-1])
    left += sum(matrix[i][:min(i, n-i-1)])
    right += sum(matrix[i][max(n-i, i+1):])
    lower += sum(matrix[i][n-i:i])

print(f'Верхняя четверть: {upper}')
print(f'Правая четверть: {right}')
print(f'Нижняя четверть: {lower}')
print(f'Левая четверть: {left}')