import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, y, x):
    if x >= N or y >= M or x < 0 or y < 0 :
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph, y-1, x) # 상
        dfs(graph, y+1, x) # 하
        dfs(graph, y, x-1) # 좌
        dfs(graph, y, x+1) # 우
        return 1
    return 0

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * (M) for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    result = 0
    for i in range(N):
        for j in range(M):
            result += dfs(graph, j, i) 
    print(result)