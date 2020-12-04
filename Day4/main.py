lines = [line.replace('\n',' ') for line in open('Day4/testData/input.txt').read().split('\n\n')]
passports = [dict( tuple(x.split(':')) for x in line.split() ) for line in lines]

def part1(p):
    return all(x in p for x in ['byr','iyr','eyr','hgt','hcl','ecl','pid'])

print('Solution 1: ', sum(part1(p) for p in passports))



def part2(p):
    return all([
        1920<= int(p['byr']) <=2002,
        2010<= int(p['iyr']) <=2020,
        2020<= int(p['eyr']) <=2030,
        p['hgt'][-2:] in ('cm','in') and ( 
            ( p['hgt'][-2:] == 'in' and 59<= int(p['hgt'][:-2]) <= 76 ) or
            ( p['hgt'][-2:] == 'cm' and 150<= int(p['hgt'][:-2]) <= 193) ),
        p['hcl'][0] == '#' and all (c in '0123456789abcdef' for c in p['hcl'][1:]),
        p['ecl'] in 'amb blu brn gry grn hzl oth'.split(),
        p['pid'].isdigit() and len(p['pid'])==9
    ])

print('Solution 2: ', sum(part1(p) and part2(p) for p in passports))
