with open(0) as file:
    lines = file.readlines()

mapping = {
        '.':'0',
        'O':'1',
        '#':'2',
}

def print_grid(grid):
    for row in grid:
        print(*row)
    print()

def go_up(grid):
    for ir, row in enumerate(grid):
        while ir > 0:
            for ic in range(len(row)):
                if grid[ir][ic] == 'O' and grid[ir-1][ic] == '.':
                    grid[ir-1][ic] = 'O'
                    grid[ir][ic] = '.'
            ir -= 1
    return grid

def rotate(grid):
    t = zip(*grid)
    rotated = []
    for r in t:
        line = []
        for c in r[::-1]:
            line.append(c)
        rotated.append(line)
    return rotated

def cycle(grid):
    for i in range(4):
        up = go_up(grid)
        rt = rotate(up)
        grid = rt
    return grid

def total_load(grid):
    res = 0
    levels = len(grid)
    for row in grid:
        acc = 0
        for col in row:
            if col == 'O':
                acc += 1
        res += acc * levels
        levels -= 1
    return res

def to_base_three(string):
    nb = 0
    for i in range(len(string)):
        nb += int(string[i])*(3**i)
    return nb

def get_hash(grid):
    hashing = []
    for row in grid:
        value = ''
        for col in row:
            value += mapping[col]
        number = to_base_three(value)
        hashing.append(number)
    return tuple(hashing)

grid = []
for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    line = [c for c in line]
    grid.append(line)

N = 1_000_000_000
counter = 1
keys = [get_hash(grid)]
for i in range(N):
    grid = cycle(grid)
    grid_hash = get_hash(grid)
    if grid_hash not in keys:
        counter += 1
        keys.append(grid_hash)
    else:
        pref = keys.index(grid_hash)
        break

loop_size = counter - pref
step_in_loop = (N-pref) % loop_size

result = set()
for i in range(step_in_loop):
    grid = cycle(grid)
    res = total_load(grid)
    result.add(res)
print(res)
