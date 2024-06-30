def lengthOfLongestSubstring(s):

    l, r = 0, 1
    tempSet = set()
    maxL = 0
    
    while r < len(s):
        if s[r] not in tempSet:
            tempSet.add(s[r])
            r += 1
        else:
            tempSet.remove(s[r])
            maxL = max(maxL, r-l+1)
            l = r
            r += 1
    return maxL




print(lengthOfLongestSubstring("aab"))