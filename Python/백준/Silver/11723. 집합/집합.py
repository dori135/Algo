import sys
input = sys.stdin.readline

a = [0 for _ in range(20)]
for _ in range(int(input())):
    op = input().split()
    if op[0] == 'add':
        a[int(op[1])-1] = 1
    elif op[0] == 'remove':
        a[int(op[1])-1] = 0
    elif op[0] == 'check':
        print(a[int(op[1])-1])
    elif op[0] == 'toggle':
        a[int(op[1])-1] = 0 if a[int(op[1])-1] == 1 else 1
    elif op[0] == 'all':
        a = [1 for _ in range(20)]
    elif op[0] == 'empty':
        a = [0 for _ in range(20)]