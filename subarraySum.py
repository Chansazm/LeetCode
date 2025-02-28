from collections import defaultdict

def subarraySum(nums,k):
    ans = curr = 0
    counts = defaultdict(int)
    counts[0] = 1
    
    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1
    return ans
        










nums = [1, 2, 1, 2, 1]
k = 3
print(subarraySum(nums,k)) #---> 4