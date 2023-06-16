n, m = [int(i) for i in input().split()]

template = [str(i) for i in range(1, m + 1)]
matrix = [template[i % m:] + template[:i % m] for i in range(n)]

for row in matrix:
    print('  '.join(row))
