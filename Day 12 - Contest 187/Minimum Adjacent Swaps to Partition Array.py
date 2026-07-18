def minAdjacentSwaps(nums: list[int], a: int, b: int) -> int:

    total_swaps = 0
    count_1 = 0
    count_2 = 0

    for num in nums:
        if num > b:
            val = 2
        elif num < a:
            val = 0
        else:
            val = 1

        if val == 0:
            total_swaps += count_1 + count_2
        elif val == 1:
            total_swaps += count_2
            count_1 += 1
        else:
            count_2 += 1

    return total_swaps

    # def bubble_sort(arr):
    #     count = 0
    #     for i in range(len(arr)):
    #         for j in range(0, len(arr) - i - 1):
    #             if arr[j] > arr[j + 1]:
    #                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #                     count += 1
    #     return count

    # for i in range(len(nums)):
    #     if nums[i] > b:
    #         nums[i] = 2
    #     elif nums[i] < a:
    #         nums[i] = 0
    #     else:
    #         nums[i] = 1

    # return bubble_sort(nums)

print(minAdjacentSwaps([1,3,2,4,5,6], 3, 4))
print(minAdjacentSwaps([9,7,5,3], 4, 8))
print(minAdjacentSwaps([3,7,5,9], 4, 8))