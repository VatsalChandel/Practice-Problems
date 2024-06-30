def maxArea(heights):
    maxArea = 0
    
    l, r = 0, len(heights) - 1
    
    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        maxArea = max(maxArea, area)
        
        if heights[l] < heights[r]:
            l += 1
        elif heights[l] >= heights[r]:
            r -= 1
    return maxArea

print(maxArea([1,7,2,5,4,7,3,6]))