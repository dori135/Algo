n = int(input())
s = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
result={}
for i in s:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
for i in c:
    if c[-1] == i:
        if i in result:
            print(result[i])
        else:
            print("0")
    else:
        if i in result:
            print(result[i], end=' ')
        else:
            print("0", end=' ')