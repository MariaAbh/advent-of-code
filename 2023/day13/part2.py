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

def dismatch(a,b):
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1
    return counter

def find_mirror_line(grid):
    mirror_indexes = []
    previous = grid[0]
    for index, line in enumerate(grid[1:]):
        count_d = dismatch(line,previous)
        if line == previous or count_d <= 1:
            mirror_indexes.append((index+1,count_d))
        previous = line

    return mirror_indexes

def is_mirror(grid,index,counter):
    side1 = index-2
    side2 = index+1
    while side1 >= 0 and side2 < len(grid):
        counter += dismatch(grid[side1],grid[side2])
        side1 -=1
        side2 +=1
        if counter > 1:
            return False
    if counter == 0:
        return False
    return True


h = []
v= []
c = 0
for pattern in grids:
    c += 1
    horizontal_index = find_mirror_line(pattern)
    if horizontal_index:
        for h_index,count_h in horizontal_index:
            if is_mirror(pattern,h_index,count_h):
                h.append(h_index*100)

    t = transpose_grid(pattern)
    vertical_index = find_mirror_line(t)
    if vertical_index:
        for v_index,count_v in vertical_index:
            if is_mirror(t,v_index,count_v):
                v.append(v_index)

res = sum(h)+sum(v)
print(res)
