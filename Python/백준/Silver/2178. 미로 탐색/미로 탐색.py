import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# 상 하 좌 우 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))
    
bfs(0,0)
print(graph[N-1][M-1])