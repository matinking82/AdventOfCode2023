inp = open('t.txt').read().split('\n')


def count(time: int, distance: int):
    counter = 0
    for j in range(1,time):
        v = j*1
        d = (time-j)*v
        if d>distance:
            counter+=1
    return counter
        

times = list(map(lambda a: int(a), filter(
    lambda a: a != '', inp[0].split(':')[1].split(' '))))
distances = list(map(lambda a: int(a), filter(
    lambda a: a != '', inp[1].split(':')[1].split(' '))))

ans = 1

for i in range(0, len(times)):
    c = count(times[i], distances[i])
    ans *= c

print(ans)