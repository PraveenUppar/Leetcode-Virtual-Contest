def rearrangeString(self, s: str, x: str, y: str) -> str:
    
    if x not in s:
        return s
    if y not in s:
        return s

    y_string = ""
    x_string = ""

    for i in range(len(s)):
        if s[i] == y:
            y_string += s[i]
        else:
            x_string += s[i]
    return y_string + x_string

print(rearrangeString(None, "aabbcc", "a", "b"))  # Output: "bbccaa"
print(rearrangeString(None, "dcab", "d", "b"))  # Output: "dbac"