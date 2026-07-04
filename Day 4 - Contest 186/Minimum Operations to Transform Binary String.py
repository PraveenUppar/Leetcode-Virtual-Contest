class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        
        if s1 == s2:
            return 0

        if s1 == "1" and s2 == "0":
            return -1

        ans = 0
        remove = []

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue

            if s1[i] == '0':      
                ans += 1
            else:                 
                remove.append(i)

        i = 0
        while i < len(remove):
            if i + 1 < len(remove) and remove[i + 1] == remove[i] + 1:
                ans += 1
                i += 2
            else:
                ans += 2          
                i += 1
        return ans