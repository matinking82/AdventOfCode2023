def count(t: str):
    inp = t.split('|')
    def f(a): return a != ''
    n1 = list(filter(f,inp[0].split(' ')))
    n2 = list(filter(f,inp[1].split(' ')))
    
    c = 0
    for j in n1:
        if j in n2:
            c+=1
            
    return c


all = open('t.txt').read().split('\n')
all = list(map(lambda t: t.split(':')[1].strip(), all))
all.insert(0, '')
print(all)

process = []
countall = len(all)-1

tt = len(all)
for i in range(1,tt):
    ct = count(all[i])
    print(f'{i}/{tt}')
    for j in range(i+1,i+ct+1):
        if j>=len(all):
            break
        process.append((j,all[j]))
        countall+=1
    
    while(len(process)>0):
        t1,t2 = process.pop()
        ctt = count(t2)
        for j in range(t1+1,t1+ctt+1):
            if j>=len(all):
                break
            process.append((j,all[j]))
            countall+=1

print(countall)
        