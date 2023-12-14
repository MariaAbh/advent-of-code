with open('input.txt', 'r') as file:
   lines = file.readlines()

integers = [str(i) for i in range(10)]
results = list()

def get_first(line):
    for c in line:
        if c in integers:
            first = c
            return first
    return '0'

def  get_last(line):
    last = '0'
    for c in line:
        if c in integers:
            last = c
    return last

for line in lines:
    first = get_first(line)
    last = get_last(line)
    if first == '0':
        res = last
    elif last == '0':
        res = first
    else:
        res = first + last
    results.append(int(res))
print(sum(results))


