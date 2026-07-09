
def maximumSaleItems(items: list[list[int]], budget: int) -> int:

    
    items.sort(key=lambda x: x[1])
    
    n = len(items)
    bought = [False] * n
    res = 0
    
    for i in range(n):
        if bought[i]:
            continue
            
        factor_i, price_i = items[i][0], items[i][1]
        
        if budget >= price_i:
            budget -= price_i
            bought[i] = True
            res += 1
            
            for k in range(i + 1, n):
                if not bought[k]:
                    factor_k = items[k][0]
                    if factor_k % factor_i == 0:
                        bought[k] = True
                        res += 1
                        
    return res




print(maximumSaleItems([[6,2],[2,6],[3,4]], 9))
print(maximumSaleItems([[2,4],[3,2],[4,1],[6,4],[12,4]], 8))