import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result[i] = v
            dfs(graph, i, visited)

n = int(input())
g = [[] for _ in range(n+1)]
result = [0 for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n+1)

dfs(g, 1, visited)

for i in range(n-1):
    print(result[i+2])