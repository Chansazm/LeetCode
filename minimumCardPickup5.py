from collections import defaultdict

def minimumCardPickup(cards):
    cardsmap = defaultdict(int)
    
    ans = float("inf")
    for i in range(len(cards)):
        if cards[i] in cardsmap:
            ans = min(ans, i-cardsmap[cards[i]] + 1 )
            
        
        cardsmap[cards[i]] = i
    return ans if ans < float("inf") else 1

nums =  [1, 2, 6, 2, 1]
print(minimumCardPickup(nums))