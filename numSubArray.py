def numSubArray(nums, k):
    left = right = ans = 0
    curr = 1
    
    for right in range(nums):
        curr *= nums[right]
        