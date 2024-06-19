def isAnagram(s, t):
    s_dict = {}

    for letters in s:
        if letters in s_dict:
            s_dict[letters] += 1
        else:
            s_dict[letters] = 1
        
    for letters in t:
        if letters in s_dict:
            s_dict[letters] -= 1
        
        else:
            return False
        
    for v in s_dict.values():
        if v != 0:
            return False
    return True

print(isAnagram("ab", "a"))

