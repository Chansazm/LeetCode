from collections import defaultdict
class Solution:
    
    def minimumCardPickup(self,cards):
        maps = defaultdict(list)
        
        for i, v in enumerate(cards):
            maps[cards[i]].append(v)
        return maps.items()

solution = Solution()
    
solution = Solution()

cards = [1,2,6,2,1]

print(solution.minimumCardPickup(cards))
