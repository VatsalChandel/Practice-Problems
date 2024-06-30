
def substring(s, k):
    i = 0
    j = 0
    
    for i in range(len(s)):
        if s[i] == k[j]:
            temp = i
        while j < len(k) and s[i] == k[j]:
            i += 1
            j += 1
        if j == len(k):
            return temp
        j = 0
    return -1

def sub_anagram(s, k):
    n = len(k)
    dk = {}
    
    for letter in k:
        if letter in dk:
            dk[letter] += 1
        else:
            dk[letter] = 1
            
    for i in range(len(s)):
        string_slice = s[i:n+i]
        ds = {}
        
        for letter in string_slice:
            if letter in ds:
                ds[letter] += 1
            else:
                ds[letter] = 1
            
        if ds == dk:
            return i
        ds = {}

assert (sub_anagram("Narendra", "aN")) == 0
assert (sub_anagram("Narendra", "ren")) == 2
assert (sub_anagram("Narendra", "dr")) == 5
assert (sub_anagram("Narendra", "en")) == 3

