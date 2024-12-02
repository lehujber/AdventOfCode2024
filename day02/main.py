inp = "inp.txt"

data = [list(map(int, a.strip().split(' '))) 
            for a in open(inp)]



#part1:
def is_safe(vals: [int]):
    if vals != sorted(vals) and vals != sorted(vals,reverse=True):
        return False
    return all([abs(a - b) - 3 <= 0 and a != b for (a,b) in zip(vals,vals[1:])])

print([is_safe(v) for v in data].count(True))

#part2
def is_safe_damped(vals: list[int]):
    if is_safe(vals):
        return True
    for i,v in enumerate(vals):
        if is_safe(vals[:i] + vals[i+1:]):
            return True
    return False

print([is_safe_damped(v) for v in data].count(True))


