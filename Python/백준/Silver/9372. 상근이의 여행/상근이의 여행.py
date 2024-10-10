import sys
input = sys.stdin.readline

def dfs(graph, v, visited, result):
    visited[v] = True
    result[0] += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, result)
        
            

for _ in range(int(input())):
    n, m = map(int, input().split())
    airplane = [[] for _ in range(n+1)]
    result = [0]
    for _ in range(m):
        a, b = map(int, input().split())
        airplane[a].append(b)
        airplane[b].append(a)
    
    visited = [False] * (n+1)

    dfs(airplane, 1, visited, result)

    print(result[0]-1)
