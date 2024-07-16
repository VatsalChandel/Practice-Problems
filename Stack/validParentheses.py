def isValid(s):
    
    vald = {")":"(", "}":"{", "]":"["}
    stack = []
    
    for item in s:
        if item in vald.values():
            stack.append(item)
        elif item in vald.keys():
            if stack == [] or vald[item] != stack.pop():
                return False
    return stack == []

print(isValid("()[][({})]"))