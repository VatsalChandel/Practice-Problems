def squeeze(s, a):
    t = ""
    for letter in s:
        if letter in a:
            t += ''
        else:
            t += letter
    return t
    
print(squeeze("Vatsal", 'a'))