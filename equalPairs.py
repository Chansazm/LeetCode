def equalPairs(grid):
    def convertTuple(grid):
        return tuple(grid)
    rows = {}
    for row in grid:
        row = convertTuple(row)
        grid[row] += 1
    return rows

grid = [[3,2,1],[1,7,6],[2,7,7]]
print(equalPairs(grid))#--->3