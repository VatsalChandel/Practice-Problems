import re 

def isPalindrome(s):
    s  = re.sub(r'\W+', '', s).lower()
    s = s.replace("_","")
    return s == s[::-1]
        

print(isPalindrome("Was it a car or a cat I saw?"))
