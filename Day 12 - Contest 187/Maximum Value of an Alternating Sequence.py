def maximumValue(n: int, s: int, m: int) -> int:
    
    last_odd = n - 1 if n % 2 == 0 else n - 2
    k = (last_odd - 1) // 2
    return s + k * (m - 1) + m

    # max_ele = s
    # current_val = s
    
    # for i in range(1, n):
    #     if i % 2 != 0:
    #         current_val = current_val + m
    #     else:
    #         current_val = current_val - 1
            
    #     if current_val > max_ele:
    #         max_ele = current_val
            
    # return max_ele

    # arr = [1] * n
    # arr[0] = s

    # for i in range(1, n):
    #     if i % 2 != 0:
    #         arr[i] = arr[i - 1] + m
    #     else:
    #         arr[i] = arr[i - 1] - 1

    # max_ele = max(arr)
    # return max_ele


print(maximumValue(5, 10, 2))  
print(maximumValue(4, 3, 5))  
print(maximumValue(2, 4, 3))  
print(maximumValue(13633232, 8009517, 57601))  