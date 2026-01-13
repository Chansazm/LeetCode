from collections import defaultdict

def minimumCardPickup(cards):
    cardsDict = defaultdict(list)
    
    for i in range(len(cards)):
        cardsDict[cards[i]].append(i)
    
    ans = float("inf")
    for key in cardsDict:
        arr = cardsDict[key]
        for i in range(len(arr)-1):
            ans = min(ans, arr[i+1]-arr[i]+1)
    return ans if ans < float("inf") else -1
    

nums =  [1, 2, 6, 2, 1]
print(minimumCardPickup(nums))