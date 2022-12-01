def groupAnagrams(strs):
    # [String] -> [[String]]

    hash_map = {}
    for i, v in enumerate(strs):
        sorted_word = "".join(sorted(v))
        if sorted_word not in hash_map:
            hash_map[sorted_word] = [i]
        else:
            hash_map[sorted_word].append(i)

    anagrams = []
    for key in hash_map:
        group = []
        for i in hash_map[key]:
            group.append(strs[i])
        anagrams.append(group)
        
    return anagrams