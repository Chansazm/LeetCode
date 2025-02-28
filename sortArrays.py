def sortArrays(arr1, arr2):
    arr = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    
    return arr

arr1 = [1,4,7,20]
arr2 = [3,5,7]
print(sortArrays(arr1, arr2))
        