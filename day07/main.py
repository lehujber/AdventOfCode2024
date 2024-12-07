input = "inp.txt"

data = [[int(t), list(map(int,l.strip().split(' ')))] for [t,l] 
    in [l.strip().split(': ') for l in open(input).readlines()]]

#part1:
def check_validity(target: int, current: int, values: [int]):
    if current != target and values == []:
        return False
    if current == target and values == []:
        return True

    [h,tail] = [values[0], values[1:]]
    return check_validity(target, current + h, tail) or \
           check_validity(target, current * h, tail)

print(sum([t for [t,vs] in data if check_validity(t, vs[0], vs[1:])]))

#part2:
def check_validity_concat(target: int, current: int, values: [int]):
    if current != target and values == []:
        return False
    if current == target and values == []:
        return True

    [h,tail] = [values[0], values[1:]]
    return  check_validity_concat(target, current + h, tail) or \
            check_validity_concat(target, current * h, tail) or \
            check_validity_concat(target, int(str(current) + str(h)), tail)

print(sum([t for [t,vs] in data if check_validity_concat(t, vs[0], vs[1:])]))
