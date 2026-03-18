def missingnumber(arr):
    n = len(arr)
    expected_xor = 0
    for i in range(n + 1):
        expected_xor ^= i
        print("expectedxor",expected_xor)
    
    # actual_xor = 0
    # for num in arr:
    #     actual_xor ^= num
    # return expected_xor ^ actual_xor
        
nums = [9,6,4,2,3,5,7,0,1]
#nums = [0,1,2,3,4,5,6,7,9]
arr = [1, 2, 4, 5, 6]#-->3
print(missingnumber(nums))