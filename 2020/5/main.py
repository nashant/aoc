from re import sub
def binSub(binString):
    return int(sub('[FL]', '0', sub('[BR]', '1', binString)), 2)

with open('input.txt', 'r') as fd:
    takenIds = sorted([binSub(l) for l in fd.read().split('\n') if l])
    print(takenIds[-1])
    print(set(range(takenIds[0], takenIds[-1] - takenIds[0])) - set(takenIds))
