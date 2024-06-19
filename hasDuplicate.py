def hasDuplicate( nums) -> bool:
    set_nums = set(nums)

    return set_nums == nums


print(hasDuplicate([1,2,3,4]))