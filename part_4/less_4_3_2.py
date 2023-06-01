# put your python code here
n = int(input())

my_list = [[j for j in range(1,i + 1)] for i in range(1,n+1)]
print(*my_list, sep='\n')