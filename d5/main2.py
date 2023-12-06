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


def converItem3(convertor:list[int],item:list[int]):
    dif = (convertor[0]-convertor[1])
    rett= list(map(lambda a: a+dif,item))
    return rett

def convertItem2(convertor:list[int],item:list[int]):
    # ll = (convertor[1]>=item[0] and convertor[1]<=item[1])
    # rr = (convertor[1]+convertor[2]>item[0] and convertor[1]+convertor[2]<item[1])
    ll = (item[0]>=convertor[1] and item[0]<convertor[1]+convertor[2])
    rr = (item[1]>=convertor[1] and item[1]<convertor[1]+convertor[2])
    
    ret = []
    if ll and rr:
        ret.append((True,converItem3(convertor,item)))          
    elif ll:
        ret.append((True,converItem3(convertor,[item[0],convertor[1]+convertor[2]-1])))
        ret.append((False,[convertor[1]+convertor[2],item[1]]))
    elif rr:
        ret.append((False,[item[0],convertor[1]-1]))
        ret.append((True,converItem3(convertor,[convertor[1],item[1]])))
    else:
        if convertor[1]<item[0] and convertor[1]+convertor[2]>item[1]:
            ret.append((False,[item[0],convertor[1]-1]))
            ret.append((True,converItem3(convertor,[convertor[1],convertor[1]+convertor[2]-1])))
            ret.append((False,[convertor[1]+convertor[2],item[1]]))
        else:
            ret.append((False,item))
    ret = list(filter(lambda a:a[1][0]!=a[1][1],ret))
    
    return ret
    
def convertItem(convertor:list[int],item:list[list[int]]):
    copy=[]
    for i in item:
        copy.extend(convertItem2(convertor,i))
    return copy
    
def convert(convertor:list[list[int]],item2:list[list[int]]):
    copy:list[list[int]] = []
    for rng in item2:
        rngsend = [rng.copy()]
        for cnv in convertor:
            rngcopy = convertItem(cnv,rngsend)
            rnng = []
            for e in rngcopy:
                if e[0]:
                    copy.append(e[1])
                else:
                    rnng.append(e[1])
            rngsend = rnng
        if len(rngsend)>0:
            copy.extend(rngsend)
    return copy

    
seeds = list(map(lambda a:int(a),filter(lambda a: a != '', seeds.split(':')[1].split(' '))))

mmp = lambda a: list(map(lambda b:int(b),a.split(' ')))

stos = list(map(mmp,stos[1:]))
stof = list(map(mmp,stof[1:]))
ftow = list(map(mmp,ftow[1:]))
wtol = list(map(mmp,wtol[1:]))
ltot = list(map(mmp,ltot[1:]))
ttoh = list(map(mmp,ttoh[1:]))
htol = list(map(mmp,htol[1:]))

pp:list[list[list[int]]] = []
for i in range(0,len(seeds),2):
    n1 = seeds[i]
    n2 = seeds[i+1]
    ans= convert(stos,[[n1,n1+n2-1],])
    ans= convert(stof,ans)
    ans= convert(ftow,ans)
    ans= convert(wtol,ans)
    ans= convert(ltot,ans)
    ans= convert(ttoh,ans)
    ans= convert(htol,ans)
    pp.append(ans)

mins = None

for i in pp:
    for j in i:
        if mins==None or j[0]<mins:
            mins = j[0]

print(mins)