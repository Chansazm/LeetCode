def findproduct(nums, k):
    left = 0
    curr = 1
    ans = 0
    
    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1
        ans += right - left + 1
    return ans


nums = [10, 5, 2, 6]
print(findproduct(nums, 100))