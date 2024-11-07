import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    age, name = list((sys.stdin.readline().split()))
    a.append([int(age), name, i])
a.sort(key = lambda x: (x[0], x[2]))
for i in range(n):
    print(a[i][0],a[i][1])