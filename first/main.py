import re


def calib(text):
    aa = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    aaa = ['one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']

    nums = []
    # print(f'text: {text}')


    # text = re.sub('oneight', 'one', text)
    # text = re.sub('twone', 'two', text)
    # text = re.sub('threeight', 'three', text)
    # text = re.sub('fiveight', 'five', text)
    # text = re.sub('sevenine', 'seven', text)
    # text = re.sub('eightwo', 'eight', text)
    # text = re.sub('eighthree', 'eight', text)
    # text = re.sub('nineight', 'nine', text)

    for i in range(len(text)):
        t = text[i]
        if t in aa:
            nums.append(int(t))
            continue

        tt = text[i:i+5]
        checkss = False
        for j in range(len(aaa)):
            if aa[j] in tt:
                checkss = True

        if i==0 and (text[1] in aa):
            nums.append(int(text[1]))

        if checkss and i!=0:
            continue


        for j in range(len(aaa)):
            if aaa[j] in tt:
                nums.append(int(aa[j]))
                print(tt)
                break

    if len(nums) == 0:
        return 0

    print(f'text: {text}, {nums}, {(nums[0]*10)+(nums[-1])}')
    return (nums[0]*10)+(nums[-1])


f = open('t.text')
a = f.read().split('\n')


count = 0

for text in a:
    ca = calib(text)
    count += ca

print(calib('x1onenpdjtwonert'))
print(count)
