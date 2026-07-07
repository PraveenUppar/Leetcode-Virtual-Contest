class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:

        res = []
        
        def backtrack(i: int, curr_s: str, cost: int, last_was_one: bool):
            if i == n:
                res.append(curr_s)
                return
            
            backtrack(i + 1, curr_s + "0", cost, False)
            
            if not last_was_one and cost + i <= k:
                backtrack(i + 1, curr_s + "1", cost + i, True)
                
        backtrack(0, "", 0, False)
        return res