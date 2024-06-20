def longestConsecutive(nums):
    temp = set(nums)
    longest = 0
    
    for numb in temp:
        length = 0
        
        while numb - length in temp:
            length += 1
        
        longest = max(longest, length)
    
    return longest


print(longestConsecutive([0,3,2,5,4,6,1,1]))