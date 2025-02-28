def lessk(nums,k):
    curr = left = ans = 0
    
    for right in range(len(nums)):
       curr *= nums[right]
       while curr >= k:
           curr //= nums[left]
           left += 1
    ans = right - left + 1
            
            
    
    return ans
        
        
        
        

nums = [10,5,2,6]
print(lessk(nums,100))