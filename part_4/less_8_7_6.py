# grades 4
set1 = set([int(n) for n in input().split()])
set2 = set([int(n) for n in input().split()])
set3 = set([int(n) for n in input().split()])
set4 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(*sorted(set4-(set1|set2|set3)))
# print(*sorted(set(range(11)) - (a | b | c)))