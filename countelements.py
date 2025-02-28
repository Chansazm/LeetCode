
def countElements(arr):
        count = 0
        dict = {}
        
        for k, v in enumerate(arr):
            dict[v] = k
        
        for i in range(len(arr)):
            if arr[i] + 1 in dict:
                count += 1
            
        return count
    
nums = [1,2,3]
print(countElements(nums)) #--> 3
