import sys
input = sys.stdin.readline

N = int(input())
pp = []
for i in range(N):
    pp.append(list(map(int, input().split())))
result = [0, 0]

def paper(a, b, n):
    check = pp[a][b]    
    for i in range(a, a + n):
        for j in range(b, b + n):
            if pp[i][j] != check:
                n //= 2
                for x in range(2):
                    for y in range(2):
                        paper(a + x * n, b + y * n, n)
                return

    if check == 0:
        result[0] += 1
    else:
        result[1] += 1
paper(0, 0, N)
for i in result:
    print(i)