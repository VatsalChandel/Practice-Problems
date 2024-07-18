def findMin(nums):
    res = nums[0]
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
            
        m = (l + r) // 2
        res = min(res, nums[m])
        
        if nums[m] < nums[r]:
            r = m - 1
        else:
            l = m + 1
    return res
  
  
print(findMin([3,4,5,6,1,2]))