from math import floor
input = "inp.txt"

data = [l[:-1] for l in open(input).readlines()]

size = len(data)
ind = ''.join(data).index('^')

g_x,g_y = floor(ind / size), ind % size

dir = (-1,0)

#part1:
rotation_map = {
    (-1,0):(0,1),
    (0,1):(1,0),
    (1,0):(0,-1),
    (0,-1):(-1,0)
}

explored = [[c for c in l] for l in data]
explored[g_x][g_y] = 'x'

while 0 < g_x and g_x < size-1 and 0 < g_y and g_y < size-1:
    g_x += dir[0]
    g_y += dir[1]

    c = explored[g_x][g_y]
    if c == '#':
        g_x -= dir[0]
        g_y -= dir[1]
        dir = rotation_map[dir]
    else:
        explored[g_x][g_y] = 'x'

print(sum([l.count('x') for l in explored]))

#part2:
#Very dumb brute force solution
n = 0
for x,l in enumerate(data):
    for y,_ in enumerate(l):
        g_x,g_y = floor(ind / size), ind % size
        dir = (-1,0)
        current = [[c for c in l] for l in data]
        current[g_x][g_y] = 'x'
        if x != g_x or y != g_y:
            current[x][y] = '#'
        iter = 0
        limit = size * size * 4
        while 0 < g_x and g_x < size-1 and 0 < g_y and g_y < size-1 and iter < limit:
            iter += 1
            g_x += dir[0]
            g_y += dir[1]

            c = current[g_x][g_y]
            if c == '#':
                g_x -= dir[0]
                g_y -= dir[1]
                dir = rotation_map[dir]
            else:
                current[g_x][g_y] = 'x'

        if iter == limit:
            n += 1

print(n)
