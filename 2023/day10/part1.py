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

prev = start_position
current = real_neighbors[0]
counter = 2
while current != real_neighbors[1]:
    for val in graph[current]:
        if val != prev:
            prev = current
            current = val
            break
    counter += 1
print(counter//2)

