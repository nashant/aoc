from math import floor, prod
with open('input.txt', 'r') as fd:
    routes = ((3, 1), (1, 1), (5, 1), (7, 1), (1, 2))
    lines = [l for l in fd.read().split('\n') if l]
    paths = [[lines[i*v][(i*h) % len(lines[i*v])] for i in range(int(len(lines)/v))] for h, v in routes]
    print(paths[0].count('#'))
    print(prod([path.count('#') for path in paths]))
