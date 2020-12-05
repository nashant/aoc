from math import floor, prod
with open('input.txt', 'r') as fd:
    routes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    lines = [l for l in fd.read().split('\n') if l]
    maxH = max([h for h, v in routes])
    lines = [(l * (1 + floor(((maxH + 1) * i + 1)/len(l)))) for i, l in enumerate(lines)]
    paths = [[lines[i * v][i * h] for i in range(int(len(lines) / v))] for h, v in routes]
    print(prod([path.count('#') for path in paths]))
