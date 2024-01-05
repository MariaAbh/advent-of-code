with open(0) as file:
    lines = file.readlines()

grid = []
grid2 = []
for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    line = [*line]
    grid.append(line)
    line1 = [*line]
    grid2.append(line1)

def behavior(direction,cell_type):
    dr,dc = direction
    if cell_type == '.':
        return [direction]
    if cell_type == '/':
        return [(-dc,-dr)]
    if cell_type == '\\':
        return [(dc,dr)]
    if cell_type == '-':
        if dr == 0:
            return [direction]
        else:
            return [(0,-1),(0,1)]
    if cell_type == '|':
        if dc == 0:
            return [direction]
        else:
            return [(-1,0),(1,0)]

grid_width = len(grid[0])
grid_height = len(grid)
direction = (0,1)
position = (0,0)
beams = [[direction,position]]
energized = 1 

show_dir = {
    (0,1):'>',
    (0,-1):'<',
    (-1,0):'^',
    (1,0):'v',
}

visited = []

def print_grid(grid,direction,position):
    ir,ic = position
    elem = grid[ir][ic]
    grid[ir][ic] = '@'
    for row in grid:
        print(*row)
    # grid[ir][ic] = show_dir[direction]
    grid[ir][ic] = '#'

while beams:
    direction,coord = beams.pop()
    if [direction,coord] not in visited:
        visited.append([direction,coord])
    # print_grid(grid2,direction,coord)
    # input()
    coord_r, coord_c = coord
    next_directions = behavior(direction,grid[coord_r][coord_c])
    # print('element,direction,next_direction',grid[coord_r][coord_c],direction,next_directions)
    for d in next_directions:
        ir = coord_r + d[0]
        ic = coord_c + d[1]
        if not (ir<0 or ic<0 or ir>=grid_height or ic>=grid_width):
            if [d,(ir,ic)] not in visited:
                # print(f'{ir,ic=}')
                energized += 1
                beams.append([d,(ir,ic)])
        # else:
        #     print(f'Eliminated {ir,ic = }')
visited_pos = {pos for d,pos in visited}
print(len(visited_pos))
