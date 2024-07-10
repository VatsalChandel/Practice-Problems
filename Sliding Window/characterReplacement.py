def characterReplacement(s: str, k: int):
    d = {}
    res = 0
    l = 0
    
    for r in range(len(s)):
        if s[r] in d:
            d[s[r]] += 1
        else:
            d[s[r]] = 1
        
        
        while (r-l + 1) - max(d.values()) > k:
            d[s[l]] -= 1
            l += 1
        
        res = max(res, r - l + 1)
        
    return res

print(characterReplacement("XYYX", 2))