# grades 2
# grades 2
set1 = set([int(n) for n in input().split()])
set2 = set([int(n) for n in input().split()])
set3 = set([int(n) for n in input().split()])

print(*sorted((set1|set2|set3)-(set1&set2&set3)))
