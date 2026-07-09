from collections import Counter

def digitFrequencyScore(n: int) -> int:

    count = Counter(str(n))
    res = 0

    for key, value in count.items():
        freq = int(key) * value
        res += freq
    return res


print(digitFrequencyScore(122))  
print(digitFrequencyScore(101))  