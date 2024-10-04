import collections
dq = collections.deque()
dq_num = collections.deque()
n = int(input())
num = list(map(int, input().split()))
for i in range(n):
    dq.append(num[i])
    dq_num.append(i)
result = []
a = dq.popleft()
a_num = dq_num.popleft()
result.append(a_num)
for t in range(n-1):
    if a < 0:
        for i in range(-1*a-1):
            b = dq.pop()
            dq.appendleft(b)
            b_num = dq_num.pop()
            dq_num.appendleft(b_num)
        a = dq.pop()
        a_num = dq_num.pop()
        result.append(a_num)
    else:
        for i in range(a-1):
            b = dq.popleft()
            dq.append(b)
            b_num = dq_num.popleft()
            dq_num.append(b_num)
        a = dq.popleft()
        a_num = dq_num.popleft()
        result.append(a_num)
for i in range(n-1):
    print(result[i]+1, end=' ')
print(result[-1]+1)