def game(text: str):

    id = int(text.split(':')[0].split(' ')[1])
    rounds = text.split(':')[1].strip().split(';')
    red =0
    green=0
    blue=0
    for round in rounds:
        r = round.split(',')
        for each in r:
            ee = each.strip()
            if 'green' in ee:
                iii = int(ee.split(' ')[0])
                if iii>green:
                    green=iii
            elif 'red' in ee:
                iii = int(ee.split(' ')[0])
                if iii>red:
                    red=iii
            elif 'blue' in ee:
                iii = int(ee.split(' ')[0])
                if iii>blue:
                    blue=iii

    print(id,red,green,blue)
    return (red*blue*green)


file = open('t.text', 'r')
a = file.read().split('\n')

count = 0
for i in a:
    aa = game(i)
    count+=aa

print(count)