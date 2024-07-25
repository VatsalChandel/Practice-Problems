def uniqueChars(s):
    t = set()
    for c in s:
        if c not in t:
            t.add(c)
        else:
            return False
    return True

def uniqueCharsN(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
            
    return True

print(uniqueCharsN("abcde"))