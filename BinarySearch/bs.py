def bs(nums, n):
    l = 0
    m = 0
    h = len(nums)-1
    
    while l <= h:
        m = (l+h)//2
        if nums[m] < n:
            l = m + 1
        elif nums[m] > n:
            h = m - 1
        else:
            return m
    return None


print(bs([ 2, 3, 4, 10, 40 ], 10))