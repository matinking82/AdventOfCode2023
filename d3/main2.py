inp = list(map(lambda a: list(a), open('t.txt').read().split('\n')))

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
w = len(inp[0])
h = len(inp)


def ratio(i, j, nums, w, h):
    s = []
    ii = i
    jj = j-1
    n1 = ''
    if i==4:
        pass
    while jj >= 0 and inp[ii][jj] in nums:
        n1 = inp[ii][jj] + n1
        jj -= 1
    if n1 != '':
        s.append(int(n1))

    ii = i
    jj = j+1
    n2 = ''
    while jj < w and inp[ii][jj] in nums:
        n2 += inp[ii][jj]
        jj += 1
    if n2 != '':
        s.append(int(n2))

    ii = i+1
    jj = j+1
    n3 = ''
    while ii < h and jj < w and inp[ii][jj] in nums:
        n3 += inp[ii][jj]
        jj += 1

    ii = i+1
    jj = j-1
    n4 = ''
    while ii < h and jj >= 0 and inp[ii][jj] in nums:
        n4 = inp[ii][jj] + n4
        jj -= 1

    if i+1 < h and inp[i+1][j] in nums:
        nn = n4+inp[i+1][j]+n3
        if nn != '':
            s.append(int(nn))
    else:
        if n3 != '':
            s.append(int(n3))
        if n4 != '':
            s.append(int(n4))

    ii = i-1
    jj = j+1
    n5 = ''
    while ii >= 0 and jj < w and inp[ii][jj] in nums:
        n5 += inp[ii][jj]
        jj += 1

    ii = i-1
    jj = j-1
    n6 = ''
    while ii >= 0 and jj >= 0 and inp[ii][jj] in nums:
        n6 = inp[ii][jj] + n6
        jj -= 1

    if i-1 >= 0 and inp[i-1][j] in nums:
        nn = n6+inp[i-1][j]+n5
        if nn != '':
            s.append(int(nn))
    else:
        if n5 != '':
            s.append(int(n5))
        if n6 != '':
            s.append(int(n6))

    if len(s)==2:
        return s[0]*s[1]
    else:
        return 0


count = 0
for i in range(h):
    for j in range(w):
        t = inp[i][j]
        if t =='*':
            check = False
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    if ii >= h or jj >= w or (ii == i and jj == j):
                        continue
                    if inp[ii][jj] in nums:
                        check = True
            if check:
                k = ratio(i, j, nums, w, h)
                print(t, i, j, k)
                count += k

print(count)
