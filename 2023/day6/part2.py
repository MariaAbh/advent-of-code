import math
with open('input_ex1.txt','r') as file:
    lines = file.readlines()
my_in = []
for line in lines:
    if line[-1]=='\n':
        line = line[:-1]
    line = line.split(':')
    line = line[1].replace(' ','')
    my_in.append(int(line))

time = my_in[0]
distance = my_in[1]
min_time = distance//time +1
max_time = time - min_time

for j in range(min_time,max_time):
    sub = time - j
    max_distance = sub*j
    if max_distance > distance:
        min_time = j
        break

for x in range(max_time,min_time,-1):
    sub = time - x
    max_distance = sub*x
    if max_distance > distance:
        max_time = x
        break
print(max_time-min_time+1)
    

