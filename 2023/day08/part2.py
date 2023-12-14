import re
import math

with open(0) as file:
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

starts = []
for k in network:
    if k[-1] == 'A':
        starts.append(k)
ends = ['']*len(starts)
counter = 0
my_count = [0]*len(starts)
cycles = [0]*len(starts)
while any(c==0 for c in cycles):
    i = 0
    while i < len(instructions):
        counter += 1
        for m in range(len(my_count)):
            my_count[m] += 1
        for s,start in enumerate(starts):
            conn = network[start]
            inst_type = instructions[i]
            starts[s] = choose_instr(conn,inst_type)
            ends[s] = starts[s][-1]
        for e,end in enumerate(ends):
            if end == 'Z':
                if cycles[e] == 0:
                    cycles[e] = my_count[e]
                my_count[e]=0

        if not any(end!='Z' for end in ends):
            break
        i += 1
        if all(cycles):
            break
    print(cycles)
print(math.lcm(*cycles))
