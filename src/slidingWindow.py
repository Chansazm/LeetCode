def sliding(nums, k):
    left = right = curr = ans = 0
    n = len(nums)
    
    for right in range(n):
        curr += nums[right]
        
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans

nums = [3, 2, 1, 3, 1, 1]
k = 5

print(sliding(nums, k)) #---> 3