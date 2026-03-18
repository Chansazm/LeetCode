from collections import defaultdict
class Solution:
    def putMap(self,lst):
        map = defaultdict(list)
        
        for i, v in enumerate(lst):
            map[cards[i]].append(i)
        return map
        
    
    



cards = [1,2,6,2,1]
solution = Solution()
print(solution.putMap(cards))