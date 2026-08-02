def countRatioSubarrays(nums: list[int], a: int, b: int) -> int:

    n = len(nums)
    ans = 0

    for i in range(n):
        even = 0
        odd = 0

        for j in range(i, n):
            if nums[j] % 2 == 0:
                even += 1
            else:
                odd += 1

            if odd > 0 and even * b <= odd * a:
                ans += 1

    return ans

    # count = 0
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         x = 0
    #         y = 0
    #         sub_arr = nums[i:j + 1]
    #         for k in sub_arr:
    #             if k % 2 == 0:
    #                 x += 1
    #             else:
    #                 y += 1
    #         if y > 0 and x/y <= a/b:
    #             count += 1
    # return count

print(countRatioSubarrays([1, 2, 1, 2], 3, 2)) # 6
print(countRatioSubarrays([2,2,1], 2, 1))
print(countRatioSubarrays([2,2,2], 1, 1))