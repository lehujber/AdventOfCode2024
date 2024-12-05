from math import floor
input = "inp.txt"

[rule_list, print_list] = open(input).read().split('\n\n')
rules = [(int(s[0]),int(s[1])) for 
        s in map(lambda x: x.split('|'), rule_list.split('\n'))]

prints = [list(map(int, s)) for 
        s in map(lambda x: x.split(','), print_list.strip().split('\n'))]

#part1:
constraints = {}
for (fst,snd) in rules:
    constraints[fst] = set()
    constraints[snd] = set()
for (fst,snd) in rules:
    constraints[snd].add(fst)

def valid_printing(print: [int]) -> bool:
    forbidden = set()
    for p in print:
        if p in forbidden:
            return False
        forbidden = forbidden.union(constraints[p])
    return True

print(sum([p[floor(len(p)/2)] for p in prints if valid_printing(p)]))

#part2:
def fix_ordering(print: [int]) -> bool:
    if len(print) == 1:
        return print

    m = floor(len(print) / 2)
    fst = print[:m]
    snd = print[m:]

    s_fst = fix_ordering(fst)
    s_snd = fix_ordering(snd)

    fixed = []
    while len(s_fst) > 0 and len(s_snd) > 0:
        f = s_fst[0]
        s = s_snd[0]
        if f in constraints[s]:
            fixed.append(s)
            s_snd.pop(0)
        else:
            fixed.append(f)
            s_fst.pop(0)

    return fixed + s_fst + s_snd

print(sum([fix_ordering(p)[floor(len(p)/2)] for p in prints if not valid_printing(p)]))
