with open('input.txt', 'r') as fd:
    lines = [l.strip().split('\n') for l in fd.read().split('\n\n') if l]
    print(f"Part 1: {sum([len(set(''.join(l))) for l in lines])}")
    print(f"Part 2: {sum([len(set.intersection(*[set(p) for p in l])) for l in lines])}")
