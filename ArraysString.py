s = "total"

def firstNonRepeat(s):

    t = {}
    r = ""
    for i in range(len(s)):
        if s[i] in t:
            t[s[i]] += 1
        else:
            t[s[i]] = 1

    for k,v in t.items():
        if v == 1:
            return k
        
s = "Battle of the Vowels: Hawaii vs. Grozny"
r = "aeiou"
def removeSpecified(s, r):
    r = list(r)
    
    for char in s:
        if char in r:
            s = s.replace(char, "")
    return s


s = "Do or do not, there is no try."
def reverseString(s):
    t = ""
    for word in s.split()[::-1]:
        t += word + " "
        
    d = []
    for word in s.split():
        d.insert(0, word)
        print(d)
    return " ".join(d)
    
    

print(firstNonRepeat(s))

print(removeSpecified(s,r))

print(reverseString(s))