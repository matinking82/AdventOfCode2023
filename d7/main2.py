inp = list(map(lambda a: a.split(' '), open('t.txt').read().split('\n')))

level = 'J23456789TQKA'


def removeCard(item: list[str], card: str):
    a = list(item[0])
    while 'J' in a:
        i = a.index('J')
        a[i] = ''

    return ''.join(a)


def replaceCard(item: list[str], card: str, rep: str):
    a = list(item[0])
    while 'J' in a:
        i = a.index('J')
        a[i] = rep

    return ''.join(a)


def finds(item: list[str], count: int):
    res = [0, '']

    for i in item[0]:
        if item[0].count(i) == count:
            if i not in res[1]:
                res[0] += 1
                res[1] += i
    return res


def maximeze(item: list[str]):
    if 'J' not in item[0]:
        return item

    res5 = finds(item, 5)
    if 'J' in res5[1]:
        return ['AAAAA', item[1]]
    res4 = finds(item, 4)

    if res4[0] > 0:
        other = removeCard(item, 'J')
        if 'J' in res4[1]:
            return [other * 5, item[1]]
        else:
            return [other+other[0], item[1]]

    res3 = finds(item, 3)

    if res3[0] > 0:
        if 'J' in res3[1]:
            other = removeCard(item, 'J')
            mx = other[0]
            if level.find(other[1]) > level.find(mx):
                mx = other[1]

            return [replaceCard(item, 'J', mx), item[1]]
        else:
            return [replaceCard(item, 'J', res3[1]), item[1]]

    res2 = finds(item, 2)

    if res2[0] == 1:
        if 'J' in res2[1]:
            other = removeCard(item, 'J')
            mx = other[0]
            if level.find(other[1]) > level.find(mx):
                mx = other[1]
            if level.find(other[2]) > level.find(mx):
                mx = other[2]

            return [replaceCard(item, 'J', mx), item[1]]
        else:
            return [replaceCard(item, 'J', res2[1]), item[1]]

    if res2[0] == 2:
        if 'J' in res2[1]:
            if res2[1][0] == 'J':
                mx = res2[1][1]
            else:
                mx = res2[1][0]

        else:
            mx = res2[1][0]
            if level.find(res2[1][1]) > level.find(mx):
                mx = res2[1][1]
        return [replaceCard(item, 'J', mx), item[1]]

    mx = ''
    mxlvl = 0

    for i in item[0]:
        if 'J' == i:
            continue
        lvl = level.find(i)
        if lvl > mxlvl:
            lvl = mxlvl
            mx = i

    return [replaceCard(item, 'J', mx), item[1]]


def fivekind(item1: list[str], item2: list[str]):
    ll1 = item1[0].count(item1[0][0]) == 5
    ll2 = item2[0].count(item2[0][0]) == 5
    if ll1 and ll2:
        return 5
    elif ll1:
        return 1
    elif ll2:
        return -1

    return 0


def fourkind(item1: list[str], item2: list[str]):
    l1 = finds(item1, 4)
    l2 = finds(item2, 4)

    if l1[0] > 0 and l2[0] > 0:
        return 5
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
        return 5
    elif ll1[0] == 0:
        return -1
    elif ll2[0] == 0:
        return 1

    return 5


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
    copy1 = item1.copy()
    copy2 = item2.copy()

    item1 = maximeze(item1)
    item2 = maximeze(item2)

    fivek = fivekind(item1, item2)
    if fivek==5:
        return highcard(copy1,copy2)
    if fivek != 0:
        return fivek

    fourk = fourkind(item1, item2)
    if fourk==5:
        return highcard(copy1,copy2)
    if fourk != 0:
        return fourk

    fhouse = fullhouse(item1, item2)
    if fhouse==5:
        return highcard(copy1,copy2)
    if fhouse != 0:
        return fhouse

    pair1 = finds(item1, 2)
    pair2 = finds(item2, 2)
    if pair1[0] > pair2[0]:
        return 1
    elif pair1[0] < pair2[0]:
        return -1

    return highcard(copy1,copy2)


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

ccc = 1
for i in inp:
    # if 'J' in i[0]: print(i,maximeze(i))
    insert(sorted, i)
    print(ccc)
    ccc += 1

for i in sorted:
    print(i)
rank = len(sorted)
ans = 0

for i in sorted:
    ans += int(i[1])*rank
    rank -= 1

print(ans)
