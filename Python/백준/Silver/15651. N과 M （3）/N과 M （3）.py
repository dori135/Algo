import itertools
n, m = map(int, input().split())
result = itertools.product(range(1, n+1), repeat = m)
for i in result:
    print(*i)