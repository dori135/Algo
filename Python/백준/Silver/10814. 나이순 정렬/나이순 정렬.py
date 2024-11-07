n = int(input())
a = []

for i in range(n):
    age, name = list((input().split()))
    a.append([int(age), name, i])
a.sort(key = lambda x: (x[0], x[2]))
for i in range(n):
    print(a[i][0],a[i][1])