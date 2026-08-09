def weightedSum(self, parent: list[int], nums: list[int]) -> int:

    n = len(parent)

    # Build the tree
    children = [[] for _ in range(n)]

    for i in range(1, n):
        children[parent[i]].append(i)

    # Find height
    height = 0

    def find_height(node, depth):
        nonlocal height

        height = max(height, depth)

        for child in children[node]:
            find_height(child, depth + 1)

    find_height(0, 1)

    # Calculate weighted sum
    total = 0

    def dfs(node, depth):
        nonlocal total

        total += nums[node] * (height - depth + 1)

        for child in children[node]:
            dfs(child, depth + 1)

    dfs(0, 1)

    return total
print(weightedSum(None, [-1,0,0,0,2,2], [5,2,3,1,4,6]))