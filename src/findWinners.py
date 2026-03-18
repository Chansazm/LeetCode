from collections import defaultdict


def findWinners(nums):
    counts = defaultdict(int)
    seen = set()
    for winner, loser in nums:
        seen.add(winner)
        seen.add(loser)
        counts[loser] += 1
    
    zero_loss, one_loss = [], []
    for player in seen:
        if counts[player] == 0:
            zero_loss.append(player)
        elif counts[player] == 1:
            one_loss.append(player)
 
    return counts







matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(findWinners(matches))#--->[[1,2,10],[4,5,7,8]]