def removeDups(s):
    t = set()
    r = ""
    for letter in s:
        if letter in t:
            r += ""
        else: 
            r += letter
        t.add(letter)
    return r

def removeDupsS(s):
    s = list(s)
    w = 1 
    
    for r in range(1, len(s)):
        dups = False
        for i in range(0, w):
            print(s[r])
            print(s[i])
            if s[r] == s[i]:
                dups = True
                break
        if not dups:
            s[w] = s[r]
            w += 1
            print(s[:w])
    
    return "".join(s[:w])
        
print(removeDupsS("Vatsal"))