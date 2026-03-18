def groupAnagrams(str):
    anagrams = {}
    for s in str:
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return list(anagrams.values())

str = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(str))#[["bat"],["nat","tan"],["ate","eat","tea"]]