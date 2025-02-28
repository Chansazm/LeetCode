def waysToSplit(nums):
    left = ans = 0
    prefix = [nums[0]]
    
    for right in range(1,len(nums)):
        prefix.append(nums[right] + prefix[-1])
    
    
    for i in range(len(nums)-1):
        left_section = prefix[i]
        right_section = prefix[-1]-prefix[i]
        
        if left_section > right_section:
            ans += 1
    return ans
        





arr = [10,4,-8,7]
print(waysToSplit(arr)) #---> 2