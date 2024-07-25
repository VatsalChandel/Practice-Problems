def anagram(s,t):
    dt = {}
        
    for letter in t:
        if letter in dt:
            dt[letter] += 1
        else:
            dt[letter] = 1
    
    for letter in s:
        if letter in dt:
            dt[letter] -= 1
            if dt[letter] < 0:
                return False
    
    for k,v in dt.items():
        if v != 0:
            return False
    
    return True

print(anagram("haat","thaa"))