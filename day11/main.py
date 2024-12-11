input = "inp.txt"

data = [int(v) for v in open(input).read().strip().split(' ')]

stones = dict()
for v in data:
    if v not in stones:
        stones[v] = 0
    stones[v] += 1

def blink(stones: dict()) -> dict():
    new_stones = dict()
    def add_new_stone(s:int ,n: int):
        if s not in new_stones:
            new_stones[s] = 0
        new_stones[s] += n

    for s,n in stones.items():
        if s == 0:
            add_new_stone(1, n)
        elif len(str(s)) % 2 == 0:
            st = str(s)
            m = int(len(st) / 2)
            add_new_stone(int(st[:m]), n)
            add_new_stone(int(st[m:]), n)
        else:
            add_new_stone(s * 2024, n)

    return new_stones

#part1:
line = stones.copy()
for _ in range(25):
    line = blink(line)

print(sum(n for (_,n) in line.items()))

#part2:
line = stones.copy()
for _ in range(75):
    line = blink(line)

print(sum(n for (_,n) in line.items()))
