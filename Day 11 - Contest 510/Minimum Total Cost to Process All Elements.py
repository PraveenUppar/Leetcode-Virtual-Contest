def minimumCost(nums: list[int], k: int) -> int:

    MOD = 10**9 + 7
    balance = k
    operations = 0
    total_cost = 0

    for need in nums:
        if balance < need:
            m = (need - balance + k - 1) // k
            total_cost += m * (2 * operations + m + 1) // 2
            total_cost %= MOD

            operations += m
            balance += m * k

        balance -= need

    return total_cost

    # balance = k
    # operations = 0
    # cost = 0

    # for num in nums:
    #     while balance < num:
    #         balance += k
    #         operations += 1
    #         cost += operations
    #     balance -= num

    # return cost

print(minimumCost([1, 2, 3, 4], 4))  # Output: 3 
print(minimumCost([1, 2, 7, 14], 4))  # Output: 15
print(minimumCost([1, 2, 3, 4], 10))  # Output: 0