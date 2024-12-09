input = "inp.txt"

data = [int(c) for c in open(input).read().strip()]

#part1:
file_system = []
for i,v in enumerate(data):
    if i % 2 == 0:
        file_system += [int(i / 2)] * v
    else:
        file_system += [-1] * v

last_file = len(file_system) - 1
first_empty = 0

compressed = file_system.copy()
while last_file > first_empty:
    if compressed[last_file] == -1:
        last_file -= 1 
    elif compressed[first_empty] != -1:
        first_empty += 1
    else:
        compressed[first_empty] = compressed[last_file]
        compressed[last_file] = -1
        first_empty += 1
        last_file -= 1

print(sum(i * v for (i,v) in enumerate([v for v in compressed if v != -1])))

#part2:
compressed = file_system.copy()
for v in sorted(set(compressed) - set([-1,0]), reverse=True):
    size = compressed.count(v)
    start = 0
    end = 0
    first_ind = compressed.index(v)
    moved = False
    while end < first_ind and not moved:
        while start < first_ind and compressed[start] != -1:
            start += 1
        end = start
        while end < first_ind and compressed[end] == -1:
            end += 1

        if end - start >= size:
            moved = True
            for offs in range(size):
                compressed[start + offs] = v 
                compressed[first_ind + offs] = -1
        else:
            start = end + 1

print(sum(i * v for (i,v) in enumerate([v if v != -1 else 0 for v in compressed])))
