from collections import defaultdict

def largestUniqueNumber(nums):
        if not nums:
            return -1
        nums.sort()
        n = len(nums) - 1
        for i in range(n, -1, -1):
            curr = nums[i]
            if curr != curr - 1:
                return curr-1
        return -1
nums = [5,7,3,9,4,9,8,3,1]
print(largestUniqueNumber(nums))