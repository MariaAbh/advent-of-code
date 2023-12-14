with open(0) as file:
    lines = file.readlines()

grids = []
current_grid = []
for line in lines:
    if line == '\n':
        grids.append(current_grid)
        current_grid = []
    else:
        line = line[:-1]
        current_grid.append(line)
grids.append(current_grid)

def print_grid(grid):
    for row in grid:
        print(row)

def transpose_grid(grid):
    h = zip(*grid)
    transposed = []
    for r in h:
        line = ''
        for e in r:
            line += e
        transposed.append(line)
    return transposed

def find_mirror_line(grid):
    mirror_indexes = []
    previous = grid[0]
    for index, line in enumerate(grid[1:]):
        if line == previous:
            mirror_indexes.append(index+1)
        previous = line
    return mirror_indexes

def is_mirror(grid,index):
    side1 = index-1
    side2 = index
    while side1 >= 0 and side2 < len(grid):
        if grid[side1] == grid[side2]:
            side1 -=1
            side2 +=1
        else:
            return False
    return True

h = []
v= []
for pattern in grids:
    horizontal_index = find_mirror_line(pattern)
    if horizontal_index:
        for h_index in horizontal_index:
            if is_mirror(pattern,h_index):
                h.append(h_index*100)

    t = transpose_grid(pattern)
    vertical_index = find_mirror_line(t)
    if vertical_index:
        for v_index in vertical_index:
            if is_mirror(t,v_index):
                v.append(v_index)

res = sum(h)+sum(v)
print(res)
