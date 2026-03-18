from collections import defaultdict
def equalPairs(grid):
    dic = defaultdict(int)
    
    for row in grid:
        dic[tuple(row)] += 1
    
    ans = 0   
    for c in zip(*grid):
        ans += dic[c]
    return ans
        

grid = [[3,2,1],[1,7,6],[2,7,7]]
print(equalPairs(grid))#--->3