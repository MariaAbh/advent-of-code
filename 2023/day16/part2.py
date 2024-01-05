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

show_dir = {
    (0,1):'>',
    (0,-1):'<',
    (-1,0):'^',
    (1,0):'v',
}


def print_grid(grid,direction,position):
    ir,ic = position
    elem = grid[ir][ic]
    grid[ir][ic] = '@'
    for row in grid:
        print(*row)
    # grid[ir][ic] = show_dir[direction]
    grid[ir][ic] = '#'

def beaming(beams):
    visited = set()
    while beams:
        direction,coord = beams.pop()
        if (direction,coord) not in visited:
            visited.add((direction,coord))
        # print_grid(grid2,direction,coord)
        # input()
        coord_r, coord_c = coord
        next_directions = behavior(direction,grid[coord_r][coord_c])
        # print('element,direction,next_direction',grid[coord_r][coord_c],direction,next_directions)
        for d in next_directions:
            ir = coord_r + d[0]
            ic = coord_c + d[1]
            if not (ir<0 or ic<0 or ir>=grid_height or ic>=grid_width):
                if (d,(ir,ic)) not in visited:
                    # print(f'{ir,ic=}')
                    beams.append([d,(ir,ic)])
            # else:
            #     print(f'Eliminated {ir,ic = }')

    visited_pos = {pos for d,pos in visited}
    return len(visited_pos)


def beaming_new(beams):
    visited = set()
    visited.add(tuple(beams[0]))
    while beams:
        direction,coord = beams.pop()
        coord_r, coord_c = coord
        next_directions = behavior(direction,grid[coord_r][coord_c])
        for d in next_directions:
            ir = coord_r + d[0]
            ic = coord_c + d[1]
            if not (ir<0 or ic<0 or ir>=grid_height or ic>=grid_width):
                if (d,(ir,ic)) not in visited:
                    visited.add((d,(ir,ic)))
                    beams.append([d,(ir,ic)])
            # else:
            #     print(f'Eliminated {ir,ic = }')

    visited_pos = {pos for d,pos in visited}
    return len(visited_pos)

max_tiles = []

left = [(row,0) for row in range(grid_height)]
right = [(row,grid_height-1) for row in range(grid_height)]
top = [(0,col) for col in range(grid_width)]
bottom = [(grid_width-1,col) for col in range(grid_width)]
print("starting left")
for pos in left:
    beams_l = []
    directions = (0,1)
    beams_l.append([directions,pos])
    tiles_l = beaming(beams_l)
    max_tiles.append(tiles_l)
print("starting right")
for pos in right:
    beams_r = []
    directions = (0,-1)
    beams_r.append([directions,pos])
    tiles_r = beaming(beams_r)
    max_tiles.append(tiles_r)
print("starting top")
for pos in top:
    beams_t = []
    directions = (1,0)
    beams_t.append([directions,pos])
    tiles_t = beaming(beams_t)
    max_tiles.append(tiles_t)
print("starting bottom")
for pos in bottom:
    beams_b = []
    directions = (-1,0)
    beams_b.append([directions,pos])
    tiles_b = beaming(beams_b)
    max_tiles.append(tiles_b)

print(max(max_tiles))
