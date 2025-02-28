from itertools import count


def consecutiveones(nums, k):
    left = 0
    ans = 0
    curr = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
            while curr > k and left < len(nums):
                if nums[left] == 0:
                    curr -= nums[left]
                left += 1
            ans = max(right - left + 1, ans)
    return ans
            
nums = [1,1,1,0,0,0,1,1,1,1,0]
print(consecutiveones(nums, 2)) #---> 6
            