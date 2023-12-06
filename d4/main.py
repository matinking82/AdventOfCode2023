def worth(text: str):
    inp = text.split('|')
    n1 = list(filter(lambda a: a != '', inp[0].strip().split(' ')))
    n2 = list(filter(lambda a: a != '',inp[1].strip().split(' ')))
    count = 0
    for j in n1:
        if j in n2:
            count += 1

    print(text, count)
    if count == 0:
        return 0
    else:
        return 2**(count-1)


all = list(map(lambda a: a.split(':')[
           1].strip(), open('t.txt').read().split('\n')))

count = 0

for i in all:
    w = worth(i)
    count += w
    print(count)

print(count)
