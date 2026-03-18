from collections import defaultdict

def groupAnagrams(strs):
    group = defaultdict(list)
    
    for s in strs:
        key = "".join(sorted(s))
        group[key].append(s)
    return group.values()
    






strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs)) #[["bat"],["nat","tan"],["ate","eat","tea"]]