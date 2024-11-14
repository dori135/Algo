N, M = map(int, input().split())
gang = list(map(int, input().split()))
start = max(gang)
end = sum(gang)
mid = (start + end) // 2
result = mid
while start <= end:
    mid = (start + end) // 2
    sum = 0
    count = 1
    for i in range(len(gang)):
        if sum + gang[i] > mid:
            sum = 0
            count += 1
        sum += gang[i]

    if count > M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)