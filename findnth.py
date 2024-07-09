def findnth(lst, n):
    lst = sorted(lst, reverse=True)
    return lst[n-1]
    
    
    
    for num in lst:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num
    
    return third

print(findnth([1,2,3,4,5,6,7,8,9], 3))