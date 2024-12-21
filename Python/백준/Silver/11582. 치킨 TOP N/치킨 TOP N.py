N = int(input())
chicken = list(map(int, input().split()))
k = int(input())

result = []
op = N // k
def merge_sort(arr, num):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left, num//2)
    right_sorted = merge_sort(right, num//2)

    if num == op:
        left = "1"
        right = "1"
        result.append(merge(left_sorted, right_sorted))
        return
    return merge(left_sorted, right_sorted)


def merge(left, right):
    if left == None or right == None:
        return

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result
t = merge_sort(chicken, N)

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end = ' ')