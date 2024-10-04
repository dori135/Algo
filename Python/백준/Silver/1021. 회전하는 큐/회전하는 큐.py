def mode2(dq):
    a = dq.popleft()
    dq.append(a)

def mode3(dq):
    a = dq.pop()
    dq.appendleft(a)
    
import collections
dq = collections.deque()
n, m = map(int, input().split())
num = list(map(int, input().split()))
for i in range(n):
    dq.append(i+1)
check = 0
result = 0
while check < m: 
    if dq[0] == num[check]:
        dq.popleft()
        check += 1
    else:
        if dq.index(num[check]) > len(dq)/2:
            mode3(dq)
            result += 1
        else:
            mode2(dq)
            result += 1
print(result)