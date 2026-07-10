def limitOccurrences(nums: list[int], k: int) -> list[int]: 

    if not nums or k == 0:
        return []  

    res = []
    sub_k = k

    for i in range(len(nums)):

        if i > 0 and nums[i] != nums[i - 1]:
            sub_k = k 

        if sub_k != 0:
            res.append(nums[i])
            sub_k -= 1

        elif sub_k == 0 and nums[i] == nums[i - 1]:
            continue
    return res

print(limitOccurrences([1, 1, 1, 2, 2, 3], 2))  # Output: [1, 1, 2, 2, 3]
print(limitOccurrences([1, 2, 3], 1))  # Output: [1, 2, 3]
print(limitOccurrences([5, 5], 1))  # Output: [5]
print(limitOccurrences([50, 75, 75], 1))  # Output: [50, 75]