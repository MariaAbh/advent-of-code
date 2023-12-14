with open('input.txt','r') as file:
    lines = file.readlines()
result = []
r = []
for line in lines:
    card = line.split(':')
    lists = card[1].split('|')
    l1 = lists[0].split(' ')
    if lists[1][-1] == '\n':
        lists[1] = lists[1][:-1]
    l2 = lists[1].split(' ')
    point = 1
    counter = 0
    for c in l1:
        if c in l2 and c != '':
            counter += 1
            if counter > 1:
                point = point*2
    if counter == 0:
        point = 0
    result.append(point)
    r.append(counter)

new_d ={i+1:1 for i in range(len(r))}
for i in range(len(r)):
    card = i+1
    nb = r[i]
    for j in range(card+1,card+nb+1):
        for x in range(new_d[card]):
            new_d[j] += 1
rs = 0
for v in new_d.values():
    rs += v
print(rs)
