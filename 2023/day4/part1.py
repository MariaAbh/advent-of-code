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
            r.append(c)
    if counter == 0:
        point = 0
    result.append(point)
print(sum(result))
