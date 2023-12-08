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

locs:list[str] = []
for i in inp:
    ii = convert(i)
    mdict[ii[0]] = ii[1:]
    if ii[0].endswith('A'):
        locs.append(ii[0])
    
inp = []

# count = 0

def check(li:list[str]):
    for j in li:
        if not j.endswith('Z'):
            return True
    return False

def getNumbers(item:str):
    count = 0
    while not item.endswith('Z'):
        for d in instruction:
            count+=1
            if d=='L':
                item = mdict[item][0]
            else:
                item = mdict[item][1]
    return count

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def lcm(x, y):
   lcm = (x*y)/gcd(x,y)
   return lcm

nums = list(map(lambda a:getNumbers(a),locs))

print(locs)
print(nums)

ans = 1

for i in nums:
    ans = lcm(ans,i)
print(ans)
# while check(locs):
#     for d in instruction:
#         for i in range(0,len(locs)):
#             if d == 'L':
#                 locs[i] = mdict[locs[i]][0]
#             else:
#                 locs[i] = mdict[locs[i]][1]
#         count+=1
#     print(locs,count)
# print(count)