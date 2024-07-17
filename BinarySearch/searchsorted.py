def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:   
        m = (l + r) // 2
        
        if nums[m] == target:
            return m
        
        if nums[l] <= nums[m]:
            if target < nums[l] or target > nums[m]:
                l = m + 1
            else:
                r = m - 1
                
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1 
            
    
print(search(nums = [5,1,3], target = 3))