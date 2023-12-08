inp = (open('t.txt').read().split('\n'))

instruction = list(inp[0])
inp = inp[2:]


def convert(item: str):
    res = []
    item = item.replace('(', '')
    item = item.replace(')', '')
    item = item.replace(',', '')
    item = item.replace(' =', '')
    return item.split(' ')


mdict: dict[str, list[str]] = {}

for i in inp:
    ii = convert(i)
    mdict[ii[0]] = ii[1:]
    
inp = []

loc = 'AAA'
count = 0

while loc!='ZZZ':
    for d in instruction:
        if d == 'L':
            loc = mdict[loc][0]
        else:
            loc = mdict[loc][1]
        count+=1
        
print(count)