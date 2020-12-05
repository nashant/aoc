from itertools import product
def binSub(binString, zero, one, reverse=False):
    if reverse:
        return binString.replace('0', zero).replace('1', one)
    return binString.replace(zero, '0').replace(one, '1')

with open('input.txt', 'r') as fd:
    cols  = [binSub(f'{i:007b}', 'F', 'B', True) for i in range(127)]
    rows  = [binSub(f'{i:003b}', 'L', 'R', True) for i in range(8)]
    taken = [(l[0:-3], l[-3:]) for l in fd.read().split('\n') if l]
    takenIds = sorted([int(binSub(r, 'F', 'B'), 2) * 8 + int(binSub(c, 'L', 'R'), 2) for r, c in taken])
    print(takenIds[-1])
    for i in range(len(takenIds)):
        if takenIds[i + 1] - takenIds[i] == 2:
            print(takenIds[i] + 1)
            exit()
