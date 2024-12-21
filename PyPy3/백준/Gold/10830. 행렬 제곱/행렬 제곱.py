import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))    

def mul(x, y):
    n = len(x)
    result = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = sum(x[i][k] * y[k][j] for k in range(n)) % 1000
    return result

def mat(A, B):
    n = len(A)
    if B == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] %= 1000
        return A
    C = mat(A, B//2)
    if B % 2 == 0:
        return mul(C, C)
    else:
        return mul(mul(C, C), A)

result = mat(A, B)
for i in result:
    for j in i:
        print(j, end=' ')
    print()