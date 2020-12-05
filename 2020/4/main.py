import re
def validate(doc):
    try:
        if not 1920 <= int(doc['byr']) <= 2002:
            return False
        if not 2010 <= int(doc['iyr']) <= 2020:
            return False
        if not 2020 <= int(doc['eyr']) <= 2030:
            return False
        if not re.match(r"^#[0-9a-f]{6}$", doc['hcl']):
            return False
        if doc['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
        if not re.match(r"^\d{9}$", doc['pid']):
            return False
        hgt = int(doc['hgt'][0:-2])
        unit = doc['hgt'][-2:]
        if unit not in ('cm', 'in'):
            return False
        if unit == 'cm' and not 150 <= hgt <= 193:
            return False
        if unit == 'in' and not 59 <= hgt <= 76:
            return False
    except:
        return False
    return True

with open('input.txt', 'r') as fd:
    docs = [doc.split(' ') for doc in fd.read().replace('\n', ' ').strip().split('  ')]
    docDicts = [{f.split(':')[0]: f.split(':')[1] for f in doc} for doc in docs]
    valid = [doc for doc in docDicts if validate(doc)]
    print(len(valid))
