from collections import defaultdict

def equalpairs2(grid):
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    
    #count the rows
    for row in grid:
        dic1[tuple(row)] += 1
    
    #count the coulumns
    for columns in range(len(grid[0])):
        column = []
        for row in range(len([grid])):
            column.append(grid[row][columns])
        dic2[tuple(column)] += 1
        
    ans = 0
    for arr in dic1:
        ans += dic1[arr] * dic2[arr]
    return ans
    
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(equalpairs2(grid))#--->3