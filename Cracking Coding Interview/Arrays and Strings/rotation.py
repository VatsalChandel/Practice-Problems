def isSubstring(s,t):
    return s in t

def rotation(s,t):
    if len(s) != len(t):
        return False
    tt = t + t
    return isSubstring(s,tt)

print(rotation("waterbottle", "erbottlewat"))