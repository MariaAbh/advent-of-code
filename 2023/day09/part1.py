with open(0) as file:
    lines = file.readlines()

dataset = []
for line in lines:
    data = line.split(' ')
    data = [int(i) for i in data]
    dataset.append(data)

def get_delta(data):
    start = data[0]
    delta_step = []
    for i in range(1,len(data)):
        delta = data[i] - start
        start = data[i]
        delta_step.append(delta)
    return delta_step

result = []
for data in dataset:
    steps = []
    sequence = data
    steps.append(sequence)
    while any(i != 0 for i in sequence):
        sequence_diff = get_delta(sequence)
        steps.append(sequence_diff)
        sequence = sequence_diff
    res = 0
    for l in steps:
        res += l[-1]
    result.append(res)
print(sum(result))
