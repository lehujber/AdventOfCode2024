input = "inp.txt"
data = [l.strip() for l in open(input).readlines()]
size = len(data)

#part1
rotated = [''.join([data[j][i] for j in range(size)]) for i in range(size)]
height_rev = [''.join([data[size-1-i][j] for j in range(size)]) for i in range(size)]

def get_diagonals(m):
    size = len(m)
    diagonals = []

    for i in range(size):
        diag = []
        for j in range(size-i):
            diag.append(m[i+j][j])
        diagonals.append(''.join(diag))

    return diagonals

diagonals = get_diagonals(data)
diagonals += get_diagonals([l[::-1] for l in data])
diagonals += get_diagonals(height_rev)[1:]
diagonals += get_diagonals([l[::-1] for l in height_rev])[1:]

c = 0
w = "XMAS"
for l in data:
    c += l.count(w)
    c += ''.join(reversed(l)).count(w)
for d in diagonals:
    c += d.count(w)
    c += ''.join(reversed(d)).count(w)
for l in rotated:
    c += l.count(w)
    c += ''.join(reversed(l)).count(w)

print(c)

#part2
c = 0
for i in range(1,size-1):
    for j in range(1,size-1):
        if data[i][j] == 'A':
            s1 = {data[i-1][j-1],data[i+1][j+1]}
            s2 = {data[i+1][j-1],data[i-1][j+1]}
            if 'M' in s1 and 'M' in s2 and 'S' in s1 and 'S' in s2:
                c+=1


            
print(c)
