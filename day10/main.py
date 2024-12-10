input = "inp.txt"

data = [[int(c) for c in l.strip()] for l in open(input).readlines()]

start_points = set()
for i,l in enumerate(data):
    for j,c in enumerate(l):
        if c == 0:
            start_points.add((i,j))

#part1:
def find_peaks(start: (int,int), grid: [[int]]) -> int:
    (x,y) = start
    if grid[x][y] == 9:
        return set([(x,y)])
    size = len(grid)
    next_steps = {(f,s) for (f,s) in {(x-1,y), (x+1,y), (x,y-1), (x,y+1)} if 
        -1 < f and f < size and -1 < s and s < size and 
        grid[f][s] == grid[x][y] + 1}

    return set.union(*[find_peaks(n, grid) for n in next_steps], set())

print(sum(len(find_peaks(s, data)) for s in start_points))

#part2:
def count_paths(start: (int,int), grid: [[int]]) -> int:
    (x,y) = start
    if grid[x][y] == 9:
        return 1
    size = len(grid)
    next_steps = {(f,s) for (f,s) in {(x-1,y), (x+1,y), (x,y-1), (x,y+1)} if 
        -1 < f and f < size and -1 < s and s < size and 
        grid[f][s] == grid[x][y] + 1}
    return sum(count_paths(s, grid) for s in next_steps)

print(sum(count_paths(s, data) for s in start_points))
