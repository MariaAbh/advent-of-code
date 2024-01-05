with open(0) as file:
    lines = file.readlines()

def hashing(word,current):
    current_value = current
    for w in word:
        ascii_code = ord(w)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    words = line.split(',')
results = []
for word in words:
    current = 0
    results.append(hashing(word,current))
print(sum(results))
