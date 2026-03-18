def missingNumber(nums):
    n = len(nums)
    arr = [-1] * (n + 1)
    
    for num in nums:
        arr[num] = num
    print(arr)
    
    
    for k, v in enumerate(arr):
        if v == -1:
            return k
    return -1
    
nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))