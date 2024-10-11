import sys
input = sys.stdin.readline

def preorder(v):
    if v != -18:
        print(chr(v+64), end='')
        preorder(g[v][0])
        preorder(g[v][1])

def inorder(v):
    if v != -18:
        inorder(g[v][0])
        print(chr(v+64), end='')
        inorder(g[v][1])

def postorder(v):
    if v != -18:
        postorder(g[v][0])
        postorder(g[v][1])
        print(chr(v+64), end='')

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n):
    a, b, c = input().split()
    g[ord(a)-64].append(ord(b)-64)
    g[ord(a)-64].append(ord(c)-64)

preorder(1)
print()
inorder(1)
print()
postorder(1)