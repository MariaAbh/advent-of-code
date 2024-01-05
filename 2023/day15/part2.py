with open(0) as file:
    lines = file.readlines()

def hashing(word):
    current_value = 0
    for w in word:
        ascii_code = ord(w)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

boxes = {}

for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    words = line.split(',')

for word in words:
    if '=' in word:
        operation = word.split('=')
        lens,focal_lens = operation
        box_nb = hashing(lens)
        if box_nb not in boxes:
            boxes[box_nb] = [[lens,focal_lens]]
        else:
            lenses = boxes[box_nb]
            changed = False
            for i in range(len(lenses)):
                if lenses[i][0] == lens:
                    lenses[i][1] = focal_lens
                    changed = True
                    break
            if not changed:
                boxes[box_nb].append([lens,focal_lens])
    elif '-' in word:
        operation = word.split('-')
        lens = operation[0]
        box_nb = hashing(lens)
        if box_nb in boxes:
            lenses = boxes[box_nb]
            for i in range(len(lenses)):
                if lenses[i][0] == lens:
                    boxes[box_nb].remove(lenses[i])
                    break

def focus_power(l,box_nb):
    focus = 0
    for i in range(len(l)):
        focus += (1+box_nb) * (i+1) * int(l[i][1])
    return focus

all_focus = []

for k,v in boxes.items():
    all_focus.append(focus_power(v,k))
print(sum(all_focus))

