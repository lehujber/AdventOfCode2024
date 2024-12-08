from itertools import combinations

input = "inp.txt"

data = [l.strip() for l in open(input).readlines()]

symbols = set(''.join(data))
symbols.remove('.')

def symbol_indices(symbol: chr, grid: [[chr]]) -> set((int,int)):
    indices = set()
    for i,v in enumerate(grid):
        for j,c in enumerate(v):
            if c == symbol:
                indices.add((i,j))

    return indices


#part1:
def antinode_position(a1: (int,int), a2: (int,int)) -> [(int,int)]:
    (x_1, y_1) = a1
    (x_2, y_2) = a2

    x_dist = x_1 - x_2
    y_dist = y_1 - y_2

    p1 = (x_1 - (2 * x_dist), y_1 - (2 * y_dist))
    p2 = (x_1 + x_dist, y_1 + y_dist)

    return [p1,p2]

grid = [[c for c in l] for l in data]
antinodes = set()
for s in symbols:
    antenna = symbol_indices(s, grid)
    for (a1,a2) in combinations(antenna, 2):
        antinodes = antinodes.union(set(antinode_position(a1, a2)))

size = len(grid)
antinodes = {(x,y) for (x,y) in antinodes if 
                -1 < x and x < size and
                -1 < y and y < size}

print(len(antinodes))

#part2:
def more_antinodes(a1: (int,int), a2: (int,int), limit: int) -> [(int,int)]:
    (x_1, y_1) = a1
    (x_2, y_2) = a2

    x_dist = x_1 - x_2
    y_dist = y_1 - y_2

    antinodes = []
    (x,y) = a1
    while -1 < x and x < limit and -1 < y and y < limit:
        antinodes.append((x,y))
        x -= x_dist
        y -= y_dist
    (x,y) = a1
    while -1 < x and x < limit and -1 < y and y < limit:
        antinodes.append((x,y))
        x += x_dist
        y += y_dist

    return antinodes

antinodes = set()
for s in symbols:
    antenna = symbol_indices(s, grid)
    for (a1,a2) in combinations(antenna, 2):
        antinodes = antinodes.union(set(more_antinodes(a1, a2, size)))

antinodes = {(x,y) for (x,y) in antinodes if 
                -1 < x and x < size and
                -1 < y and y < size}
print(len(antinodes))
