def missingNumber2(nums):
    n = len(nums)
    sum = 0
    total = n * (n + 1)//2
    for i in range(len(nums)):
        sum += nums[i]
    return total - sum

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber2(nums))