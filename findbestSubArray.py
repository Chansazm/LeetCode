def findBestSubArray(arr, k):
    curr = 0
    for i in range(k):
        curr += arr[i]
    
    ans = curr  
    for i in range(k, len(arr)):
        curr += arr[i] - arr[i-k]
        ans = max(ans, curr)
    return ans
        






array = [3,-1,4,12,-8,5,6]
k = 4
ans = findBestSubArray(array, k)
print(ans) #----> 18