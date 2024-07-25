def replaceSpace(s):
    for letter in s:
        if letter == " ":
            s = s.replace(letter, "%20")
    return s

def betterReplace(s):
    s = list(s)
    
    for i in range(len(s)):
        if s[i] == " ":
            s.remove(s[i])
            s.insert(i, '%20')
    return "".join(s)
    
print(betterReplace("Va ts al"))