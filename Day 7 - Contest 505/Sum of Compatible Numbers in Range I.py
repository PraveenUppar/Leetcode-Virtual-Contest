def sumOfGoodIntegers(n: int, k: int) -> int:

    comp_sum = 0

    for x in range(1000 + 1):
        if abs(n - x) <= k and (n & x) == 0:
            comp_sum += x
    return comp_sum

print(sumOfGoodIntegers(2, 3))  # Output: 10
print(sumOfGoodIntegers(1, 100))  # Output: 2550
print(sumOfGoodIntegers(5, 100))  # Output: 1378