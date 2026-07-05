def maxDigitRange(nums: list[int]) -> int:

    ans = 0
    digit_range_values = []

    for num in nums:
        max_no = max(str(num))
        min_no = min(str(num))
        digit_range = int(max_no) - int(min_no)
        digit_range_values.append(digit_range)

    max_digit_range = max(digit_range_values)

    for i in range(len(digit_range_values)):
        if digit_range_values[i] == max_digit_range:
            ans += nums[i]

    return ans

print(maxDigitRange([5724,111,350]))  
print(maxDigitRange([123, 456, 789, 321, 654]))  