
nums = [1,2,3,4,5,6,7]
target = 33

def binarySearch(nums, target, lower=None, upper=None):
    if lower == None:
        lower = 0
        upper = len(nums) - 1


    nums = nums[lower:upper+1]
    if len(nums) == 1 and nums[0] != target:
        return -1
    
    m = (upper - lower) // 2
    if nums[m] > target:
        return binarySearch(nums, target, lower, m - 1)
    elif nums[m] < target:
        return binarySearch(nums, target, m + 1, upper)
    else:
        return upper - m
        


def print_permutations(s):
    def permute(prefix, remaining):
        if len(remaining) == 0:
            print(prefix)
        else:
            for i in range(len(remaining)):
                new_prefix = prefix + remaining[i]
                new_remaining = remaining[:i] + remaining[i+1:]
                permute(new_prefix, new_remaining)

    permute("", s)

print_permutations("hat")

    

print(binarySearch(nums, target))
