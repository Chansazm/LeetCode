from collections import defaultdict
def intersection(nums):
    counts = defaultdict(int)
    for arr in nums:
        for x in arr:
            counts[x] += 1
    
    ans = []
    n = len(nums)
    for key in counts:
        if counts[key] == n:
            ans.append(key)
    return ans
    
    
    
    







nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,9999,6]]
print(intersection(nums)) #---> [3,4]