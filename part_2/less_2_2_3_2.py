digits = [int(c) for c in input().split()]

for i in range(1, len(digits), 2):
    digits[i - 1], digits[i] = digits[i], digits[i - 1]

print(*digits)
