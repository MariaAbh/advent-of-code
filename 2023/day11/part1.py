with open(0) as file:
    lines = file.readlines()

grid = []

for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    line = [c for c in line]
    grid.append(line)
    if '#' not in line:
        grid.append([*line])

def print_grid():
    for row in grid:
        print(row)

def add_column(col):
    for row in range(len(grid)):
        grid[row].insert(col,'.')

points = []
row_len = len(grid[0])
col = 0
counter = 0
while col < row_len:
    is_empty = True
    for row in range(len(grid)):
        if grid[row][col] == '#':
            points.append((row,col))
            counter += 1
            grid[row][col] = str(counter)
            is_empty = False
    if is_empty:
        add_column(col)
        col += 1
        row_len += 1
    col += 1

print_grid()
def find_distance(start,end):
    x_steps = abs(start[0]-end[0])
    y_steps = abs(start[1]-end[1])
    return x_steps+y_steps

total = 0
for start in range(len(points)-1):
    for end in range(start+1,len(points)):
        distance = find_distance(points[start],points[end])
        total += distance
print(total)
