def twoSum(nums, target):
    temp = {}

    for index, nums in enumerate(nums):

        diff = target - nums
        if diff in temp:
            return (temp[diff], index)

        temp[nums] = index

print(twoSum([3,4,5,6], 7))

