with open('input.txt','r') as file:
    lines = file.readlines()

grid = []
result = []

for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    grid.append(line)


integers = [str(i) for i in range(10)]

def check_window(r,c,l_line):
    r_start = r-1
    c_start = c-1
    r_end = r+2
    c_end = c+2

    if r == 0:
        r_start = r
    if c == 0:
        c_start = c
    if r >= l_line-1:
        r_end = l_line
    if c >= l_line-1:
        c_end = l_line

    for row in range(r_start,r_end):
        for col in range(c_start,c_end):
            elem = grid[row][col]
            if elem != '.' and elem not in integers:
                return True
    return False

def find_int(r,c,l_line):
    digit = grid[r][c]
    last_index = c+1
    for i in range(c+1,len(line)):
        elem = grid[r][i]
        if elem in integers:
            digit += elem
            last_index += 1
        else:
            break
    return digit, last_index

for row,line in enumerate(grid):
    l_line = len(line)
    col = 0
    while col < l_line:
        if grid[row][col] in integers:
            digit, last_index = find_int(row,col,l_line)
            for i in range(col,last_index):
                if check_window(row,i,l_line):
                    result.append(int(digit))
                    break
            col = last_index
        else:
            col += 1

print(sum(result))
