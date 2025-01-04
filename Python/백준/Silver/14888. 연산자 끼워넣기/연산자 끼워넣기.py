import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
d, b, g, n = map(int, input().split())
opt = [0] * d + [1] * b + [2] * g + [3] * n
import itertools
result = itertools.permutations(opt, N-1)
result = set(result)
check = []
for i in result:
    re = A[0]
    for j in range(N-1):
        if i[j] == 0:
            re += A[j+1]
        elif i[j] == 1:
            re -= A[j+1]
        elif i[j] == 2:
            re *= A[j+1]
        elif i[j] == 3:
            if re < 0:
                re = -(-re // A[j+1])
            else:
                re //= A[j+1]
    check.append(re)
print(max(max(check), -10**9))
print(min(min(check), 10**9))
