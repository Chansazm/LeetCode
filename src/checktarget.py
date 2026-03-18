def checkTarget(arr, target):
    n = len(arr)-1
    left = 0
    right = n
    
    while left < right:
         
        sum = arr[left] + arr[right]
        if sum == target:
            return True
        elif sum > target:
            right -= 1
        else:
            left += 1
        
    return False
checkTarget([1, 2, 4, 6, 8, 9, 14, 15], 13) #--> true
       






nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13

print(checkTarget(nums, target)) #--> true