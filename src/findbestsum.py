def findbestsum(nums, k):
    curr = 0
    ans = 0
    
    for i in range(k):
        curr += nums[i]
    ans = curr
    
    for right in range(k, len(nums)):
        curr += nums[right] - nums[right - k]
        
        ans = max(ans, curr)
    return ans

nums = [3,-1,4,12,-8,5,6]
print(findbestsum(nums, 4)) #--> 18