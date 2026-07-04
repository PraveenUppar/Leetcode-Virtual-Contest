class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:

        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
            
        mid = len(nums) // 2
        mid_value = nums[mid]
        
        count = 0
        for num in nums:
            if num == mid_value:
                count += 1
                
        return count == 1
