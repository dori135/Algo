from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, n, check):
    check[n] = 1
    print(n+1, end=' ')
    for i in graph[n]:
        if not check[i]:
            dfs(graph, i, check)

def bfs(graph, n, check):
	queue = deque([n])
	check[n] = 1
	while queue:
		v = queue.popleft()
		print(v+1, end=' ')
		for i in graph[v]:
			if not check[i]:
				queue.append(i)
				check[i] = 1
                
N, M, V = map(int, input().split())
graph = [[] for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(N):
    graph[i].sort()

check1 = [0 for i in range(N)]
dfs(graph, V-1, check1)
print("")
check2 = [0 for i in range(N)]
bfs(graph, V-1, check2)

