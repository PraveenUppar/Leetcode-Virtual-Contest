def maxTotal(self, nums: List[int], s: str) -> int:

    max_val = 0
    mini = float("inf")

    for i in range(len(s) - 1, -1, -1):

        if s[i] == "1":
            max_val += nums[i]
            mini = min(mini, nums[i])

        else:
            # Left boundary of a block of 1's
            if i + 1 < len(s) and s[i + 1] == "1":
                max_val += nums[i]
                mini = min(mini, nums[i])
                max_val -= mini

            # Reset for the next block
            mini = float("inf")

    return max_val

    # Greedy approach -- 385/999 testcase
    # max_val = 0

    # for i in range(len(s)):
    #     if s[i] == "1":
    #         max_val += nums[i]

    # curr_sum = 0
    # s = list(s)
    
    # for i in range(len(s)):
    #     if s[i] == "0":
    #         continue
    #     else:
    #         if i == 0:
    #             curr_sum += nums[i]  
    #         elif s[i - 1] == "0" and nums[i - 1] >= nums[i]:
    #             s[i] = "0"
    #             curr_sum += nums[i - 1]
    #         else:
    #             curr_sum += nums[i]
                
    # max_val = max(curr_sum, max_val)
    # return max_val

print(maxTotal([11, 11, 14, 10], "1011")) #36 but the code ouput is 35 
print(maxTotal([9, 2, 6, 1], "0101")) 
print(maxTotal([5, 1, 4], "001")) 
print(maxTotal([9, 3, 5], "011")) 
print(maxTotal([61], "1")) # 61