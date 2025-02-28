class Solution:
    def countElements(self, arr):
        map = {}
        count = 0
        
        for v in arr:
            if v in map:
                map[v] += 1
                count += 1
            else:
                map[v] = 1
        print(map)
        for k,v in enumerate(map):
            if k + 1 in map:
                count += 1
        print(count)
            
        

arr = [1,2,2,3]
arr2 = [1,1,3,3,5,5,7,7]
Solution().countElements(arr2)