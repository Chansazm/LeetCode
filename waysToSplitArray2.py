def waysToSplitArray2(nums):
    left_Section = 0
    total = sum(nums)
    ans = 0
   
    
    for right in range(len(nums)-1):
        left_Section += nums[right]
        right_Section = total - left_Section
        if left_Section >= right_Section:
            ans += 1
    return ans
    
    
    


arr = [10,4,-8,7]
print(waysToSplitArray2(arr)) #----> 2