with open("input.txt") as f: 
    grid = [list(line.strip()) for line in f]


ROWS, COLS = len(grid), len(grid[0])

count = 0 
directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for a in range(ROWS):
    for b in range(COLS):
        if grid[a][b] == '@': 
            neighbors = 0
            for i, j in directions: 
                if (a+i>= 0 and a+i < ROWS and b+j >=0 and b+j < COLS):
                    neighbors += (grid[a+i][b+j] == '@')

            count += (neighbors <= 3)
            #print(f"{a}-{b} has {neighbors} neighbors")

print(count)





