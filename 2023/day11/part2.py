with open(0) as file:
    lines = file.readlines()

def print_grid():
    for row in grid:
        print(row)

def find_distance(start,end):
    x_steps = abs(start[0]-end[0])
    y_steps = abs(start[1]-end[1])
    return x_steps+y_steps

grid = []

for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    line = [c for c in line]
    grid.append(line)

counter = 1
for ir, row in enumerate(grid):
    for ic, col in enumerate(row):
        if col == '#':
            grid[ir][ic] = str(counter)
            counter += 1

dict_m = {}
row_cord = []
next_index_row = 0
for ir,row in enumerate(grid):
    for e in row:
        if e !='.':
            dict_m[e]=[ir+next_index_row]
        if all(c=='.' for c in row):
            next_index_row += 999999
            break

col_cord = []
row_len = len(grid[0])
col = 0
counter = 0
next_index_col = 0
while col < row_len:
    is_empty = True
    for row in range(len(grid)):
        elem = grid[row][col]
        if elem != '.':
            dict_m[elem].append(col+next_index_col)
            is_empty = False
    if is_empty:
        next_index_col += 999999
    col += 1

total = 0
points = [v for v in dict_m.values()]
for start in range(len(points)-1):
    for end in range(start+1,len(points)):
        distance = find_distance(points[start],points[end])
        total += distance
print(total)

