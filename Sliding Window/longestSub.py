def lengthOfLongestSubstring(s):
    st = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in st:
            print(s[r])
            st.remove(s[l])
            l += 1
        st.add(s[r])
        res = max(res, r - l + 1)
    return res




print(lengthOfLongestSubstring("zxyaaaazxyz"))