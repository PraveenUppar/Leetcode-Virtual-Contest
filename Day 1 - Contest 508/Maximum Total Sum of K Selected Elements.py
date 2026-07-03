def maxSum(nums: list[int], k: int, mul: int) -> int:
    
    nums.sort(reverse = True)
    ans = 0
    # [9, 6, 2, 1]

    for i in range(k):
        if mul > 0:
            curr = nums[i] * mul
            ans += curr
            mul -= 1
        else:
            ans += nums[i]
            mul -= 1
    return ans
