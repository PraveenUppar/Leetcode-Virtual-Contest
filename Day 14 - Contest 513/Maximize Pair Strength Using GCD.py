
import math

def maxPairStrength(nums: list[int]) -> int:

    # if len(nums) <= 1 :
    #     return 1
        
    # nums.sort()
    # i = len(nums) - 2
    # j = len(nums) - 1

    # res = (nums[i] * nums[j]) / (math.gcd(nums[i], nums[j])) ** 2
    # return int(res)

    max_res = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            res = (nums[i] * nums[j]) / (math.gcd(nums[i], nums[j])) ** 2
            max_res = max(res, max_res)
    return int(max_res)

print(maxPairStrength([1, 2, 3, 4, 5]))
print(maxPairStrength([2,3,5]))
print(maxPairStrength([4, 6, 8]))
print(maxPairStrength([7, 18, 12])) # 126
print(maxPairStrength([3,3]))