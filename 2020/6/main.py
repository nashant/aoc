lines = [l.strip().split('\n') for l in "".join(open('input.txt', 'r')).split('\n\n')]
print(f"Part 1: {sum([len(set(''.join(l))) for l in lines])}")
print(f"Part 2: {sum([len(set.intersection(*[set(p) for p in l])) for l in lines])}")
