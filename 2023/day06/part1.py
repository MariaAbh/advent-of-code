import math
with open('input.txt','r') as file:
    lines = file.readlines()
my_in = []
for line in lines:
    if line[-1]=='\n':
        line = line[:-1]
    line = line.split(':')
    nb = line[1].split(' ')
    nb = [int(i) for i in nb if i != '']
    my_in.append(nb)

time = my_in[0]
distance = my_in[1]

nb_ways = []
for i in range(len(time)):
    my_time = time[i]
    my_distance = distance[i]
    points = 0
    for j in range(my_time):
        sub = my_time - j
        max_distance = sub*j
        if max_distance > my_distance:
            points += 1
    nb_ways.append(points)

print(math.prod(nb_ways))
