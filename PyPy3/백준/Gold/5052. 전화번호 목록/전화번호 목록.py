t = int(input())
che = 0
for i in range(0, t):
    n = int(input())
    call =[]
    for j in range(0, n):
        call.append(input())
    call.sort()
    for j in range(1, j+1):
        l = len(call[j]) if len(call[j]) < len(call[j-1]) else len(call[j-1])
        che = 0
        if call[j][:l] == call[j-1][:l]:
            che = 1
            break
    if che == 1:
        print("NO")
    else:
        print("YES")