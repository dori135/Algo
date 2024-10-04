import collections
dq = collections.deque()
n, k = map(int, input().split())
for i in range(n):
    dq.append(i+1)
result = []
sum = 0
while len(dq) != 0:
    if sum == k-1:
        sum = 0
        result.append(dq.popleft())
    else:
        a = dq.popleft()
        dq.append(a)
        sum += 1
print("<", end="")
for i in range(n-1):
    print(result[i], end=', ')
print(result[-1], end=">")