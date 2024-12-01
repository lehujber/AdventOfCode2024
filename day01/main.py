inp = "inp.txt"

data = [tuple(map(int, filter(lambda x: x != '', a.strip().split(' '))))
    for a in open(inp).readlines()]

col1 = [fst for (fst,_) in data]
col2 = [snd for (_,snd) in data]

#part1
print(sum([abs(a - b) for (a,b) in zip(sorted(col1),sorted(col2))]))

#part2
print(sum([a * col2.count(a) for a in col1]))
