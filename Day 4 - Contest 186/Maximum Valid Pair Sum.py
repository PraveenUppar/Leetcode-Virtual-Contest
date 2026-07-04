class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:

        best = nums[0]
        ans = 0

        for j in range(k ,len(nums)):
            best = max(best, nums[j - k])
            ans = max(ans, best + nums[j])
        return ans

        # max_val = 0
        # i = 0
        # for j in range(k, len(nums)):
        #     while i <= j - k:
        #         max_val = max(max_val, nums[i] + nums[j])
        #         i += 1
        #     i = 0
        # return max_val

        # i = 0
        # max_val = 0
        # for j in range(k, len(nums)):
        #     if j - i >= k:
        #         max_val = max(max_val, nums[i] + nums[j])
        #     i += 1
        # return max_val
        
        # max_val = 0
        # for i in range(len(nums)):
        #     for j in range(i + k, len(nums)):
        #         max_val = max(max_val, nums[i] + nums[j])
        # return max_val
