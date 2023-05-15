# put your python code here
s = [int(num) for num in input().split()]
s[0],s[1:] = s[-1], s[:-1]
print(*s)
