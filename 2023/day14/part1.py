with open(0) as file:
    lines = file.readlines()

def print_grid(grid):
    for row in grid:
        print(*row)

grid = []
for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    line = [c for c in line]
    grid.append(line)

for ir, row in enumerate(grid):
    while ir > 0:
        for ic in range(len(row)):
            if grid[ir][ic] == 'O' and grid[ir-1][ic] == '.':
                grid[ir-1][ic] = 'O'
                grid[ir][ic] = '.'
        ir -= 1

res = 0
levels = len(grid)
for row in grid:
    acc = 0
    for col in row:
        if col == 'O':
            acc += 1
    res += acc * levels
    levels -= 1
print(res)
