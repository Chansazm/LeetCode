from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards):
        MapCards = defaultdict(list)
        
        for i,v in enumerate(cards):
            MapCards[cards[i]].append(i)
        
        ans = float('inf')
        for key in MapCards:
            arr = MapCards[key]
            for i in range(len(arr)-1):
                ans = min(ans, arr[i+1]- arr[i]+1)
            
        return ans if ans < float('inf') else -1
        
    
    

cards = [1,2,6,2,1]
solution = Solution()
print(solution.minimumCardPickup(cards)) # {1:[0,4], 2:[1,3], 6:[3]}
