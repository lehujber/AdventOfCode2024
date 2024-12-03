import re
from itertools import dropwhile, takewhile

input = "inp.txt"

data = [l.strip() for l in open(input).readlines()]

def parse_mul(m: str) -> int:
    nums = ''.join(takewhile(lambda x: x != ')', dropwhile(lambda x: x != '(', m)))[1:].split(',')
    return int(nums[0]) * int(nums[1])

#part1
pattern_mul = 'mul\\([1-9][0-9]?[0-9]?,[1-9][0-9]?[0-9]?\\)'
s = 0
d = ''.join(data)
for d in data:
    s += sum(parse_mul(m) for m in re.findall(pattern_mul, d))
print(s)

#part2
pattern_do = 'do\\(\\)'
pattern_dont = 'don\'t\\(\\)'

pattern_full = pattern_mul + '|' + pattern_do + '|' + pattern_dont

active = True
s = 0
for d in data:
    inst = re.findall(pattern_full, d)
    ind = 0
    while ind < len(inst):
        curr = inst[ind]
        if curr == "don't()":
            active = False
        if curr == "do()":
            active = True
        if curr not in ["do()","don't()"] and active:
            s += parse_mul(curr)
        ind += 1

print(s)

