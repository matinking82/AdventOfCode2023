inp = list(map(lambda a: a.split(' '), open('t.txt').read().split('\n')))

level = '23456789TJQKA'


def finds(item: list[str], count: int):
    res = [0, '']

    for i in item[0]:
        if item[0].count(i) == count:
            if i not in res[1]:
                res[0] += 1
                res[1] += i
    return res


def fivekind(item1: list[str], item2: list[str]):
    if item1[0]=='JJJJJ' or item2[0]=='JJJJJ':
        pass
    ll1 = item1[0].count(item1[0][0]) == 5
    ll2 = item2[0].count(item2[0][0]) == 5
    if ll1 and ll2:
        return highcard(item1, item2)
    elif ll1:
        return 1
    elif ll2:
        return -1

    return 0


def fourkind(item1: list[str], item2: list[str]):
    l1 = finds(item1, 4)
    l2 = finds(item2, 4)

    if l1[0] > 0 and l2[0] > 0:
        return highcard(item1, item2)
    elif l1[0] > 0:
        return 1
    elif l2[0] > 0:
        return -1

    return 0


def fullhouse(item1: list[str], item2: list[str]):
    l1 = finds(item1, 3)
    l2 = finds(item2, 3)
    if l1[0] == 0 and l2[0] == 0:
        return 0
    elif l1[0] == 0:
        return -1
    elif l2[0] == 0:
        return 1

    ll1 = finds(item1, 2)
    ll2 = finds(item2, 2)

    if ll1[0] == 0 and ll2[0] == 0:
        return highcard(item1, item2)
    elif ll1[0] == 0:
        return -1
    elif ll2[0] == 0:
        return 1

    return highcard(item1, item2)


def highcard(item1: list[str], item2: list[str]):

    for i in range(0, len(item1[0])):
        lvl1 = level.find(item1[0][i])
        lvl2 = level.find(item2[0][i])

        if lvl1 > lvl2:
            return 1
        elif lvl2 > lvl1:
            return -1
    return 0


def compare(item1: list[str], item2: list[str]):
    fivek = fivekind(item1, item2)
    if fivek != 0:
        return fivek

    fourk = fourkind(item1, item2)
    if fourk != 0:
        return fourk

    fhouse = fullhouse(item1, item2)
    if fhouse != 0:
        return fhouse

    pair1 = finds(item1, 2)
    pair2 = finds(item2, 2)
    if pair1[0] > pair2[0]:
        return 1
    elif pair1[0] < pair2[0]:
        return -1

    return highcard(item1, item2)


def insert(li: list[list[str]], item: list[str]):
    if len(li) == 0:
        li.append(item)
        return
    i = 0
    
    while i < len(li):
        if compare(item, li[i]) != -1:
            li.insert(i, item)
            return
        i += 1
    li.append(item)


sorted: list[list[str]] = []

for i in inp:
    insert(sorted, i)

print(sorted)

rank = len(sorted)
ans = 0

for i in sorted:
    ans += int(i[1])*rank
    rank -= 1

print(ans)
