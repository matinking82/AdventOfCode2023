inp = open('t.txt').read().split('\n')

seeds = inp[0]
inp = inp[1:]

stos = []
stof = []
ftow = []
wtol = []
ltot = []
ttoh = []
htol = []

count = 0
for i in inp:
    if i == '':
        count += 1
        continue

    if count == 1:
        stos.append(i)
    elif count == 2:
        stof.append(i)
    elif count == 3:
        ftow.append(i)
    elif count == 4:
        wtol.append(i)
    elif count == 5:
        ltot.append(i)
    elif count == 6:
        ttoh.append(i)
    elif count == 7:
        htol.append(i)


def convert(lst: list[str], item: int):
    c = True
    for j in lst:
        if c:
            c = False
            continue

        ip = list(map(lambda a: int(a), j.split(' ')))
        if item >= ip[1] and item < ip[1]+ip[2]:
            ans = ip[0]+(item-ip[1])
            return ans

    return item

seeds = list(filter(lambda a: a != '', seeds.split(':')[1].split(' ')))

print(seeds)

min = None

for seed in seeds:
    s = int(seed)
    soil = convert(stos, s)
    fer = convert(stof, soil)
    water = convert(ftow, fer)
    lll = convert(wtol, water)
    temp = convert(ltot, lll)
    h = convert(ttoh, temp)
    location = convert(htol, h)

    if min == None or location < min:
        min = location

print(min)
