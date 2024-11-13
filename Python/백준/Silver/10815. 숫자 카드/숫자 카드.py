import sys
input = sys.stdin.readline

N = int(input())
n = set(list(map(int, input().split())))
M = int(input())
m = list(map(int, input().split()))

for i in m:
    if i in n:
        print(1, end=' ')
    else:
        print(0, end=' ')