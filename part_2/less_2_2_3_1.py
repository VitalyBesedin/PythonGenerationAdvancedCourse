# put your python code here
s = list(map(int, input().split()))
s[:-1:2], s[1::2] = s[1::2], s[:-1:2]
print(*s)
