n = int(input())
a = ['a','n','t','o','n']
for i in range(1,n+1):
    s = input()
    flag = 1
    for c in a:
        if s.find(c) != -1:
            s = s[s.find(c)+1:]
        else:
            flag = 0
            break
    if flag == 1:
        print(i, end=' ')

