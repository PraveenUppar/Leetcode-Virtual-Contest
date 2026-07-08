def consecutiveSetBits(n: int) -> bool:

    binary = bin(n)[2:]
    res = False
    left = 0
    k = 0

    for right in range(1, len(binary)):
        if k == 0 and binary[right] == "1" and binary[left] == "1":
            res = True
            k += 1
            left += 1
        elif k != 0 and binary[right] == "1" and binary[left] == "1":
            res = False
            left += 1
            k += 1
        else:
            left += 1

    return res

    # binary = bin(n)
    # print(binary)

    # left = 0

    # for right in range(1, len(binary)):
    #     if binary[right] == binary[left]:
    #         return True
    #     else:
    #         left += 1
    return False

print(consecutiveSetBits(3))
print(consecutiveSetBits(6))
print(consecutiveSetBits(12)) # True
print(consecutiveSetBits(15)) # False
print(consecutiveSetBits(45)) # True