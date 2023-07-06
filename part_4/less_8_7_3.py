# grades
set1 = set([int(n) for n in input().split()])
set2 = set([int(n) for n in input().split()])
set3 = set([int(n) for n in input().split()])
set1.intersection_update(set2)
set1.difference_update(set3)
print(*sorted(set1, reverse=True))
