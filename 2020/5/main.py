from re import sub
with open('input.txt', 'r') as fd:
    taken = [l for l in fd.read().split('\n') if l]
    ids = sorted([int(sub('[FL]', '0', sub('[BR]', '1', s)), 2) for s in taken])
    print(ids[-1])
    print(set(range(ids[0], ids[-1] - ids[0])) - set(ids))
