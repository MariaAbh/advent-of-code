import re


def grouped(l, step):
    return zip(*[iter(l)]*step)

def intersect(r1,r2):
    min_r1,max_r1 = r1
    min_r2,max_r2 = r2
    
    start = max(min_r1,min_r2)
    end = min(max_r1,max_r2)

    if start < end:
        return (start,end)
    else:
        return ()

def inter_diff(r1,r2):
    min_r1 = r1[0]
    min_r2 = r2[0]
    max_r1 = r1[1]
    max_r2 = r2[1]
    t_r_1 = None
    t_r_2 = None
    t_l_1 = None
    t_l_2 = None
    if min_r1 < min_r2:
        t_r_1 = min_r1
        t_r_2 = min_r2-1
    if max_r1 > max_r2:
        t_l_1 = max_r2+1
        t_l_2 = max_r1

    if t_r_1 == None and t_l_1 == None:
        return (),()
    if t_r_1 == None:
        return  (),(t_l_1,t_l_2)
    if t_l_1 == None:
        return (t_r_1,t_r_2),()
    return (t_r_1,t_r_2),(t_l_1,t_l_2)


if __name__ == '__main__':
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
    more = ''

    for s,r in grouped(seeds_nb,2):
        current = s
        r_range = r+s-1
        range_to_map = []
        range_to_map.append((current,r_range))
        range_to_map_temp = []
        for k,v in types.items():
            for r in range_to_map:
                no_mapping = True
                for l in v:
                    min_r = l[1]
                    max_r = l[1]+l[2]-1
                    s_range = r
                    c_range = (min_r,max_r)
                    inter = intersect(s_range,c_range)
                    delta = l[1]-l[0]
                    if inter:
                        no_mapping = False
                        idiff = inter_diff(s_range,inter)
                        map_inter = (inter[0]-delta,inter[1]-delta)
                        range_to_map_temp.append(map_inter)
                        for tupl in idiff:
                            if tupl:
                                range_to_map.append(tupl)

                if no_mapping == True and r not in range_to_map_temp:
                    range_to_map_temp.append(r)
            range_to_map = range_to_map_temp
            range_to_map_temp = []
        locations.extend(range_to_map)
print(min(locations)[0])

