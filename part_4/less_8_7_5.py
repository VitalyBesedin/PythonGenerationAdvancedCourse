# grades 3
set1 = set([int(n) for n in input().split()])
set2 = set([int(n) for n in input().split()])
set3 = set([int(n) for n in input().split()])

print(*sorted(set3-(set1|set2), reverse=True))
