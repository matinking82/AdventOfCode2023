def game(text: str):

    id = int(text.split(':')[0].split(' ')[1])
    rounds = text.split(':')[1].strip().split(';')

    for round in rounds:
        r = round.split(',')
        for each in r:
            ee = each.strip()
            if 'green' in ee:
                iii = int(ee.split(' ')[0])
                if iii>13:
                    return (False, id)
            elif 'red' in ee:
                iii = int(ee.split(' ')[0])
                if iii>12:
                    return (False, id)
            elif 'blue' in ee:
                iii = int(ee.split(' ')[0])
                if iii>14:
                    return (False, id)

    return (True, id)
    


file = open('t.text', 'r')
a = file.read().split('\n')

count = 0
for i in a:
    aa = game(i)
    print(aa)
    if aa[0]:
        count += aa[1]

print(count)