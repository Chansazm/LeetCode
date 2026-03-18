from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards):
        map = defaultdict(int)
        
        ans = float("inf")
        for i in range(len(cards)):
            if cards[i] in map:
                ans = min(ans,i-map[cards[i]]+1)
            
            
            
            map[cards[i]] = i
        return ans if ans < float("inf") else -1


cards = [1,2,6,2,1]
solution = Solution()
print(solution.minimumCardPickup(cards))#3