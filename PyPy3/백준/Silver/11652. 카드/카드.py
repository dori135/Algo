import collections
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

b = collections.Counter(a)
answer = max(list(b.values()))
c = list(b.items())

c.sort(key=lambda x: (x[0], x[1]))

for x, y in list(c):
    if y == answer:
        print(x)
        break