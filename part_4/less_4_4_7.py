# put your python code here
n = int(input())
matrix = [[int(_) for _ in input().split()] for _ in range(n)]

top_quarter = 0
right_quarter = 0
lower_quarter = 0
left_quarter = 0

for i in range(n):
    for j in range(n):
        if i > j and i < n - 1 - j:
            left_quarter += matrix[i][j]
        elif i < j and i > n - 1 - j:
            right_quarter += matrix[i][j]
        elif i < j and i < n - 1 - j:
            top_quarter += matrix[i][j]
        elif i > j and i > n - 1 - j:
            lower_quarter += matrix[i][j]
        else:
            continue

print("Верхняя четверть:", top_quarter)
print("Правая четверть:", right_quarter)
print("Нижняя четверть:", lower_quarter)
print("Левая четверть:", left_quarter)
