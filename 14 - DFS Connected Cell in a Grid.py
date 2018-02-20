
def getBiggestRegion(grid):
    rowGrid = len(grid)
    colGrid = len(grid[0])
    regions = {}
    maxSize = 0
    nextLabel = 2
    neighborsDif = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for r in range(rowGrid):
        for c in range(colGrid):
            if (grid[r][c] == 1):
                regions[nextLabel] = [(r, c)]
                grid[r][c] = nextLabel
                pointer = 0
                # Push all neighbors to regions[nextLabel] with BFS and change their labels = nextLabel
                while (pointer < len(regions[nextLabel])):
                    for dif in neighborsDif:
                        (x, y) = add(regions[nextLabel][pointer], dif)
                        if ((x < 0) | (y < 0) | (x >= rowGrid) | (y >= colGrid)):
                            continue
                        if (grid[x][y] != 1):
                            continue
                        regions[nextLabel].append((x, y))
                        grid[x][y] = nextLabel
                    pointer += 1
                maxSize = maxSize if (maxSize > pointer) else pointer
                nextLabel += 1
    return(maxSize)

def add(x, y):
    return((x[0] + y[0], x[1] + y[1]))

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
