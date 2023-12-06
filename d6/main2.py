inp = open('t.txt').read().split('\n')


def count(time: int, distance: int):
    counter = 0
    for j in range(1,time):
        v = j*1
        d = (time-j)*v
        if d>distance:
            counter+=1
    return counter
        

times = list(filter(
    lambda a: a != '', inp[0].split(':')[1].split(' ')))
distances = list(filter(
    lambda a: a != '', inp[1].split(':')[1].split(' ')))

time = ''
for i in times:
    time += i

distance = ''
for i in distances:
    distance+=i

print(count(int(time),int(distance)))