def minPrice(self, prices: list[int], discounts: list[int]) -> float:
    prices.sort(reverse = True)
    discounts.sort(reverse = True)

    for i in range(len(discounts)):
        prices[i] = (prices[i] * (100 - discounts[i])) / 100

    return sum(prices)