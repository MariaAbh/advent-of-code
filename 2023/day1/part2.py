with open('input.txt', 'r') as file:
   lines = file.readlines()

integers = [str(i) for i in range(10)]
string_ints = ['one','two','three','four','five','six','seven','eight','nine']
results = list()
str_num = {'one':'1',
           'two':'2',
           'three':'3',
           'four':'4',
           'five':'5',
           'six':'6',
           'seven':'7',
           'eight':'8',
           'nine':'9'}

def get_str(line):
    int_str = ''
    index = 0
    start_index = 0
    end_index = start_index+1
    str_len = len(line)
    while start_index < str_len-3:
        subword = line[start_index:end_index]
        if subword not in string_ints:
            if len(subword)>5:
                start_index += 1
                end_index = start_index+1
            else:
                end_index += 1
        else:
            return subword

def get_str_first(line):
    int_str = ''
    index = 0
    start_index = 0
    end_index = start_index+1
    str_len = len(line)

    while start_index < str_len:
        subword = line[start_index:end_index]
        if subword not in string_ints:
            c = line[start_index]
            if c in integers:
                return c
            if len(subword)>4 or end_index > str_len:
                start_index += 1
                end_index = start_index+1
            else:
                end_index += 1
        else:
            return str_num[subword]
    return int_str

def get_str_last(line):
    int_str = ''
    index = 0
    start_index = 0
    end_index = start_index+1
    str_len = len(line)
    last_word = ''
    while end_index <= str_len:
        c = line[end_index-1]
        subword = line[start_index:end_index]
        if subword not in string_ints:
            if len(subword)>4:
                start_index += 1
                end_index = start_index+1
            else:
                end_index += 1
            if c in integers:
                last_word = c
        else:
            if end_index > start_index:
                if c in integers:
                    last_word = c
                else:
                    last_word = str_num[subword]
            start_index += 1
            end_index = start_index+1
    return last_word

def  get_last(line):
    last = '0'
    for c in line:
        if c in integers:
            last = c
    return last

def main():    
    for line in lines:
        int_str_first = get_str_first(line)
        int_str_last = get_str_last(line)
        res = int_str_first + int_str_last
        results.append(int(res))
    print(sum(results))

main()
