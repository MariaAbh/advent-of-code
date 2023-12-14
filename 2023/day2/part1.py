with open('input.txt', 'r') as file:
   lines = file.readlines()

max_red = 12
max_green = 13
max_blue = 14
result = []

for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    game = line.split(':')
    game_id = int(game[0].split(' ')[1])
    turns = game[1].split(';')
    guide = True
    for turn in turns:
        dice_count = {}
        dice = turn.split(',')
        for d in dice:
            nb = int(d[1:].split(' ')[0])
            color = d[1:].split(' ')[1]
            if color in dice_count:
                dice_count[color] += nb
            else:
                dice_count[color] = nb
        for k,v in dice_count.items():
            if k == 'red':
                if v > 12:
                    guide = False
            if k == 'blue':
                if v > 14:
                    guide = False
            if k == 'green':
                if v > 13:
                    guide = False
    if guide == True:    
        result.append(game_id)
print(sum(result))
