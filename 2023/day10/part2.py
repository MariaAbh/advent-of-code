with open(0) as file:
    lines = file.readlines()

grid = []

for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    line = [c for c in line]
    grid.append(line)

north = (-1,0)
south = (1,0)
east = (0,1)
west = (0,-1)

pipes = {
        '|':[north,south],
        '-':[east,west],
        'L':[north,east],
        'J':[north,west],
        '7':[south,west],
        'F':[south,east],
        '.':[],
        'S':[north,south,east,west],
}
graph = {}

def generate_graph(symbol,row,col):
    graph[(row,col)] = []
    directions = pipes[symbol]
    for direction in directions:
        row_dir = direction[0]+row
        col_dir = direction[1]+col
        graph[(row,col)].append((row_dir,col_dir))

def print_grid(grid):
    for row in grid:
        print(*row)

for ir,row in enumerate(grid):
    for ic,elem in enumerate(row):
        generate_graph(elem, ir, ic)
        if elem == 'S':
            start_position = (ir,ic)

real_neighbors = []
start_neighbors = graph[start_position]
for neighbor in start_neighbors:
    if neighbor in graph:
        if start_position in graph[neighbor]:
            real_neighbors.append(neighbor)
graph[start_position] = real_neighbors

row_len = len(grid[:])
col_len = len(grid[0])
loop_grid = [[' ']*col_len for i in range(row_len)]

loop = []
prev = start_position
loop.append(prev)
current = real_neighbors[0]
counter = 2
while current != real_neighbors[1]:
    loop.append(current)
    for val in graph[current]:
        if val != prev:
            prev = current
            current = val
            break
    counter += 1
loop.append(current)

for elem in loop:
    loop_grid[elem[0]][elem[1]] = '#'

def vecteur_diff(a,b):
    return (b[0]-a[0],b[1]-a[1])

delta = [vecteur_diff(i,j) for i,j in zip(loop[:-1],loop[1:])]
delta.append(vecteur_diff(loop[-1],loop[0]))
delta2 = [vecteur_diff(i,j) for i,j in zip(loop[:-1],loop[1:])]
delta2.insert(0,vecteur_diff(loop[-1],loop[0]))

red = []
blue = []
outside = ''
for i in range(len(loop)):
    bi_dir = []
    bi_dir.append(delta[i])
    if delta[i] != delta2[i]:
        bi_dir.append(delta2[i])

    for deltai in bi_dir:
        dir_row, dir_col = deltai
        coord_x, coord_y = loop[i]
        if dir_row == 1 or dir_row == -1:
            right = (coord_x, coord_y-dir_row)
            left = (coord_x, coord_y+dir_row)
        if dir_col == 1 or dir_col == -1:
            right = (coord_x+dir_col , coord_y)
            left = (coord_x-dir_col, coord_y)
        
        r1, r2 = right
        l1, l2 = left

        if r1<0 or r2<0 or r1>=row_len or r2>=col_len:
            outside = 'B'
            continue
        if l1<0 or l2<0 or l1>=row_len or l2>=col_len:
            outside = 'R'
            continue

        if grid[r1][r2] == '.' or (r1,r2) not in loop:
            loop_grid[r1][r2] = 'B'
            if right not in blue:
                blue.append(right)
        if grid[l1][l2] == '.' or (l1,l2) not in loop:
            loop_grid[l1][l2] = 'R'
            if left not in red:
                red.append(left)

def add_to_list(symbol,ir,ic):
    if symbol == 'R':
        red.append((ir,ic))
    else:
        blue.append((ir,ic))

def fill(ir,ic,grid,symbols):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    symbol = grid[ir][ic]
    for dr,dc in directions:
        index_r,index_c = dr+ir, dc+ic
        if index_r < 0 or index_c < 0 or index_r >= len(grid) or index_c >= len(grid[0]):
            continue
        if grid[index_r][index_c] == ' ':
            grid[index_r][index_c] = symbol
            add_to_list(symbol,ir,ic)
            symbols.append((index_r,index_c))

def fill_grid(grid,symb):
    symbols = []
    for ir,row in enumerate(grid):
        for ic,col in enumerate(row):
            if col == symb:
                symbols.append((ir,ic))
                while symbols:
                    fill(*symbols.pop(),grid,symbols)

fill_grid(loop_grid,'R')
fill_grid(loop_grid,'B')

res = 0    
if outside == '':
    min_b = min(blue)
    min_r = min(red)
    if min_b < min_r:
        outside = 'B'
    else:
        outside = 'R'

if outside == 'B':
    res = len(red)
else:
    res = len(blue)

print(f'{res=}')
