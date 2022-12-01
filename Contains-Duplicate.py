def containsDuplicate(nums):

    # [Int] -> Bool

    nums_set = set()
    for v in nums:
        if v not in nums_set:
            nums_set.add(v)
        else:
            return True
    return False

print(containsDuplicate([1,1,3]))
