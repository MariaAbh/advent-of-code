with open('input.txt','r') as file:
    lines = file.readlines()

instructions = [c for c in lines[0][:-1]]
network = {}
for line in lines[2:]:
    if line[-1] == '\n':
        line = line[:-1]
    node,connections = line.split(' = ')
    connections = connections[1:-1].split(', ')
    network[node] = connections

def choose_instr(tupl,i):
    if i == 'R':
        return tupl[1]
    else:
        return tupl[0]

start = 'AAA'
counter = 0
while start != 'ZZZ':
    i = 0
    while i < len(instructions):
        counter += 1
        conn = network[start]
        inst_type = instructions[i]
        start = choose_instr(conn,inst_type)
        i += 1

print(counter)
