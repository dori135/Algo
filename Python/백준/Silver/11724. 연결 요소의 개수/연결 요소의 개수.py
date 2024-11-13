import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

result = 0
check = [0 for i in range(N)]

def dfs(graph, n, check):
    check[n] = 1
    for i in graph[n]:
        if not check[i]:
            dfs(graph, i, check)

for i in range(N):
    if not check[i]:
        dfs(graph, i, check)
        result += 1

print(result)