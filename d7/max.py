inp = list(map(lambda a: a.split(' '), open('tt.txt').read().split('\n')))

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
            if res2[1][0]=='J':
                mx = res2[1][1]
            else:
                mx = res2[1][0]
                
        else:
            mx = res2[1][0]
            if level.find(res2[1][1]) > level.find(mx):
                mx = res2[1][1]
        return [replaceCard(item, 'J', mx), item[1]]
            
            

    return [replaceCard(item, 'J', 'A'), item[1]]

file = open('maxt.txt','w')
for i in inp:
    print(i)
    i.append(maximeze(i)[0])
    file.write(' '.join(i)+'\n')
    
file.close()