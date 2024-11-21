import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
    
for i in range(N):
    graph[i].sort(reverse=True)

check = [0 for i in range(N)]

result = [0 for i in range(N)]
t = 1

def dfs(graph, n, check):
    global t
    check[n] = 1
    result[n] = t
    for i in graph[n]:
        if not check[i]:
            t += 1
            dfs(graph, i, check)

dfs(graph, R-1, check)


for i in result:
    print(i)