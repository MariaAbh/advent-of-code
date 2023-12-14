with open('input.txt','r') as file:
    lines = file.readlines()

cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def find_type(hand):
    count_cards = {}
    for c in hand:
        if c in count_cards:
            count_cards[c] += 1
        else:
            count_cards[c] = 1

    distinct_cards = len(count_cards)
    if distinct_cards == 1:
        return 'Five'
    elif distinct_cards == 5:
        return 'High'
    elif distinct_cards == 4:
        return 'One'
    else:
        if distinct_cards == 2:
            if 4 in count_cards.values():
                return 'Four'
            else:
                return 'Full'
        if distinct_cards == 3:
            if 3 in count_cards.values():
                return 'Three'
            else:
                return 'Two'

categories = [[] for i in range(7)]
hand_categories = ['High','One','Two','Three','Full','Four','Five']

for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    hand,score = line.split(' ')
    hand_type = find_type(hand)
    index = hand_categories.index(hand_type)
    categories[index].append((hand,score))

for c in categories:
    if len(c) > 1:
        i = 0
        j = 1
        for i in range(len(c)):
            for j in range(0,len(c)-i-1):
                hand1,score1 = c[j]
                hand2, score2 = c[j+1]
                x = 0
                while hand1[x] == hand2[x]:
                    x += 1
                if cards.index(hand1[x]) > cards.index(hand2[x]):
                    temp = c[j]
                    c[j] = c[j+1]
                    c[j+1] = temp
cat_count = 0
cat_scores = []
for l in categories:
    if l:
        cat_score = 0
        cat_count += 1
        for index in range(len(l)):
            h,s = l[index]
            sub_score = cat_count+index
            cat_score += sub_score*int(s)
        cat_scores.append(cat_score)
        cat_count = sub_score


print(sum(cat_scores))




