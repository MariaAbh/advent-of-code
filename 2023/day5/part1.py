import re

with open('input.txt','r') as file:
    lines = file.readlines()

types = {}
seed = ''
line_type = ''

for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    if 'seeds:' in line:
        seed += line
        continue
    if line == '\n' or line == '':
        line_type = ''
        continue
    else:
        if 'to' in line:
            r = re.search('-to-(.*) map:',line)
            key = r.group(1)
            line_type = key
            types[line_type] = []
        else:
            l = [int(c) for c in line.split() if c != '']
            types[line_type].append(l)

seeds = seed.split(':')
seeds_nb = [int(c) for c in seeds[1].split(' ') if c != '']

s_map = {}
g_s_map = {}
locations = []
for s in seeds_nb:
    current = s
    for k,v in types.items():
        mapped = current
        for l in v:
            min_r = l[1]
            max_r = l[1]+l[2]-1
            if min_r <= mapped <= max_r:
                sub_r = mapped-min_r
                current = l[0]+sub_r
        s_map[k]=current
    locations.append(s_map['location'])
print(min(locations))

