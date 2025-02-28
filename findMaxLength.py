def findMaxLength(nums):
    result = 0
    counts = {}
    zero, one = 0, 0
    
    for i,v in enumerate(nums):
        if v == 0:
            zero += 1
        else:
            one += 1
            
        result = max(result, i+1)
            
    return result


nums = [0,1]
print(findMaxLength(nums))#2

