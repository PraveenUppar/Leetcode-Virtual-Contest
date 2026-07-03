def countValidSubarrays(nums: list[int], x: int) -> int:
    n = len(nums)
    count = 0

    def first_digit(num):
        num = abs(num)
        if num == 0:
            return 0
        while num >= 10:
            num //= 10
        return num

    for l in range(n):
        s = 0
        for r in range(l, n):
            s += nums[r]
            last = abs(s) % 10
            first = first_digit(s)
            if first == x and last == x:
                count += 1

    return count

    # Wrong approach
    # count = 0

    # for i in range(len(nums)):
    #     if nums[i] == x:
    #         count += 1
    #     for j in range(i + 1, len(nums)):
    #         num = str(nums[i] + nums[j])
    #         if int(num[0]) == x and int(num[-1]) == x:
    #             count += 1
    # return count 

print(countValidSubarrays([1,100,1], 1))  

# You are given an integer array nums and an integer digit x.

# A subarray nums[l..r] is considered valid if the sum of its elements satisfies both of the following conditions:

# The first digit of the sum is equal to x.
# The last digit of the sum is equal to x.
# Return the number of valid subarrays.