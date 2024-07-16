def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""

    countT, window = {}, {}
    for c in t:
        if c in countT:
            countT[c] += 1
        else:
            countT[c] = 1

    have, need = 0, len(countT)
    res = [-1, -1] 
    l = 0

    for r in range(len(s)):
        c = s[r]

        if c in window:
            window[c] += 1
        else:
            window[c] = 1

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            res = [l, r]

            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l : r + 1]



print(minWindow(s = "OUZODYXAZV", t = "XYZ"))
