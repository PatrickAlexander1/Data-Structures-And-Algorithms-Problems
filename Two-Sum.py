def twoSum(nums, target):

    hash_map = {}
    for v in nums:
        if v not in hash_map:
            hash_map[v] = 1
        else:
            hash_map[v] += 1

    for key in hash_map:
        diff = target - key
        if diff in hash_map and diff != key:
            return True
        elif key == diff and hash_map[key] > 1:
            return True

    return False