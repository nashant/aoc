with open('input.txt', 'r') as fd:
    lines = [x for x in fd.read().split('\n') if x]

    #for i in range(len(lines)):
    #    policy, password = lines[i].split(': ')
    #    mn, mx, c = policy.replace('-', ' ').split(' ')
    #    n = password.count(c)
    #    if n < int(mn) or n > int(mx):
    #        lines[i] = ''

    for i in range(len(lines)):
        policy, password = lines[i].split(': ')
        mn, mx, c = policy.replace('-', ' ').split(' ')
        n = password.count(c)
        if password[int(mn)-1] == c and password[int(mx)-1] == c:
            lines[i] = ''
        if password[int(mn)-1] != c and password[int(mx)-1] != c:
            lines[i] = ''

    print(len([x for x in lines if x]))
