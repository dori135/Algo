def find_tree(tree, m, start, end):
    if start > end:
        return end
    mid = (start + end) // 2
    sum = 0
    for i in range(len(tree)-1, -1, -1):
        if tree[i] < mid:
            break
        sum += tree[i] - mid
    if sum == m:
        return mid
    elif sum > m:
        return find_tree(tree, m, mid+1, end)
    elif sum < m:
        return find_tree(tree, m, start, mid-1)
    
n, m = map(int,input().split()) 
tree = list(map(int,input().split()))
tree.sort()
print(find_tree(tree, m, 0, tree[len(tree)-1]))