from re import sub
ids = sorted([int(sub('[FL]', '0', sub('[BR]', '1', s)), 2) for s in open('input.txt', 'r')])
print(ids[-1])
print(set(range(ids[0], ids[-1] - ids[0])) - set(ids))
