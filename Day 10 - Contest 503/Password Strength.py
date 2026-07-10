def passwordStrength(password: str) -> int:

    point = 0
    unique_chars = set(password)
    
    for ch in unique_chars:
        if ch.islower():
            point += 1
        elif ch.isupper():
            point += 2
        elif ch.isdigit():
            point += 3
        elif ch in "!@#$":
            point += 5
            
    return point

    # point = 0
    # pass_set = list(set(password))
    # small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # large = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # nums = ['0','1','2','3','4','5','6','7','8','9']
    # special = ['!', '@', '#', '$']

    # for i in range(len(pass_set)):
    #     if pass_set[i] in small:
    #         point += 1
    #     elif pass_set[i] in large:
    #         point += 2
    #     elif pass_set[i] in nums:
    #         point += 3
    #     elif pass_set[i] in special:
    #         point += 5
    # return point
    
print(passwordStrength("aA1!"))
print(passwordStrength("bbB11#"))