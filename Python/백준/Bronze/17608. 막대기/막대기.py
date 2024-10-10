import sys

a = []
n = int(sys.stdin.readline())
for i in range(n):
    a.append(int(sys.stdin.readline()))
max = a[n-1]
num = 1
for i in range(2, n+1):
    if max < a[n-i]:
        max = a[n-i]
        num += 1
print(num)