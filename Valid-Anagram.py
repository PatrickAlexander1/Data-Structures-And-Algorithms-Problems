def validAnagram(s, t):
    # (String, String) -> Bool
    hash_map1 = {}
    hash_map2 = {}

    for v in s:
        if v in hash_map1:
            hash_map1[v] += 1
        else:
            hash_map1[v] = 1

    for v in t:
        if v in hash_map2:
            hash_map2[v] += 1
        else:
            hash_map2[v] = 1

    if len(hash_map1) != len(hash_map2):
        return False

    for key in hash_map1:
        if key not in hash_map2:
            return False
        if hash_map1[key] != hash_map2[key]:
            return False

    return True