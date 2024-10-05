import collections
dq = collections.deque()
n = int(input())
k = int(input())

board = [([0]*n) for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 'a'
L = int(input())
info = []
for _ in range(L):
    X, c = input().split()
    info.append((int(X), c))

d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동 남 서 북

result = 1 # 시간
dir = 0 # 기본은 동쪽
x, y, l_check = 0, 0, 0

while True:
    dq.appendleft((x,y))
    x += d[dir][0]
    y += d[dir][1]
    
    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 's':
        break

    if board[x][y] != 'a':
        p, q = dq.pop()
        board[p][q] = 0
    
    board[x][y] = 's'
        
    if l_check < len(info) and info[l_check][0] == result:
        if info[l_check][1] == 'D':
            dir = (dir+1) % 4
        elif info[l_check][1] == 'L':
            dir = (dir-1) % 4
        l_check += 1
    result += 1
print(result)