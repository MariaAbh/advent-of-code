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
    dice_count = {}
    for turn in turns:
        dice = turn.split(',')
        for d in dice:
            nb = int(d[1:].split(' ')[0])
            color = d[1:].split(' ')[1]
            if color in dice_count:
                if dice_count[color] < nb:
                    dice_count[color] = nb
            else:
                dice_count[color] = nb
    power = 1
    for v in dice_count.values():
        power *= v
    result.append(power)
print(sum(result))
