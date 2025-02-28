def preFixSum(nums):
    #psum = [nums[0]]
    
    for i in range(1,len(nums)):
        nums[i] = nums[i]+nums[i-1]
        #psum.append(nums[i] + psum[i-1])
    return nums








nums = [1,6,3,2,7,2]
print(preFixSum(nums))#---> 