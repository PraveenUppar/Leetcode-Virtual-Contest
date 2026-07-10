from collections import deque

def minOperations(nums: list[int]) -> int:
    
    target = sorted(nums)

    if nums == target:
        return 0

    queue = deque([(nums, 0)])
    visited = {tuple(nums)}

    while queue:
        curr, ops = queue.popleft()

        # Operation 1: Reverse
        rev_arr = curr[::-1]
        if rev_arr == target:
            return ops + 1
        if tuple(rev_arr) not in visited:
            visited.add(tuple(rev_arr))
            queue.append((rev_arr, ops + 1))

        # Operation 2: Rotate Left
        rot_arr = curr[1:] + [curr[0]]
        if rot_arr == target:
            return ops + 1
        if tuple(rot_arr) not in visited:
            visited.add(tuple(rot_arr))
            queue.append((rot_arr, ops + 1))

    return -1


print(minOperations([0,2,1]))      # 2
print(minOperations([1,0,2]))      # 2
print(minOperations([2,0,1,3]))    # -1
print(minOperations([0,1,2,3]))    # 0