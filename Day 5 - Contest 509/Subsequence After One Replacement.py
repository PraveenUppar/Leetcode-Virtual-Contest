
def canMakeSubsequence(s: str, t: str) -> bool:

    if len(t) < len(s): #-- Failed some test cases 993/1000
        return False 
    s_list = list(s)
    k = -1
    for i in range(min(len(s_list), len(t))):
        if s_list[i] == t[i]:
            continue
        if k != 0:
            s_list[i] = t[i]
            k += 1 
        else:
            break
    "".join(s_list)
    i = 0
    j = 0
    while i < len(s_list) and j < len(t):
        if s_list[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)   

    # if len(t) < len(s): -- Failed some test cases
    #     return False
    # i = 0
    # j = 0
    # used = 0
    # while i < len(s) and j < len(t):
    #     if s[i] == t[j]:
    #         i += 1
    #         j += 1
    #     elif used == 0:
    #         used = 1
    #         i += 1
    #         j += 1
    #     else:
    #         j += 1
    # if i < len(s):
    #     used += len(s) - i
    # return used <= 1

    # def isSubsequence(x): -- TLE
    #     i = 0
    #     j = 0
    #     while i < len(x) and j < len(t):
    #         if x[i] == t[j]:
    #             i += 1
    #         j += 1
    #     return i == len(x)
    # # no replacement
    # if isSubsequence(s):
    #     return True
    # # replace one character
    # for i in range(len(s)):
    #     original = s[i]
    #     for ch in "abcdefghijklmnopqrstuvwxyz":
    #         if ch == original:
    #             continue
    #         new_s = s[:i] + ch + s[i+1:]
    #         if isSubsequence(new_s):
    #             return True
    # return False       
        
        
print(canMakeSubsequence("cat", "chat")) # True
print(canMakeSubsequence("plane", "apple")) # False
print(canMakeSubsequence("ws", "xwxt")) # True