import sys
input = sys.stdin.readline

N = []
for _ in range(int(input())):
    N.append(int(input()))

n = max(N)
a = [0] * (n + 1)
b = [0] * (n + 1)

a[0], b[0] = 1, 0

if n > 0:
    a[1], b[1] = 0, 1

for i in range(2, n+1):
    a[i] = a[i-1] + a[i-2]
    b[i]  = b[i-1] + b[i-2]

for i in N:
    print(a[i], b[i])

