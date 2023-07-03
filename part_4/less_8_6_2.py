# General numbers
s1 = set([int(n) for n in input().split()])
s2 = set([int(n) for n in input().split()])
# l = list(s1&s2)
# l.sort()
# print(*l)
print(*sorted(s1&s2))
