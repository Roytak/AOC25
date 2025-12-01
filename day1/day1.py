
data = []

with open('in.txt') as f:
    for line in f:
        line = line.strip()
        d = line[0]
        v = int(line[1:])
        data.append((d, v))

def part1():
    cnt = 0
    c = 50

    for d, v in data:
        if d == 'L':
            c -= v
        else:
            c += v
        c = c % 100
        if c == 0:
            cnt += 1

    return cnt

def part2():
    cnt = 0
    c = 50
    zero = 0

    for d, v in data:
        if v >= 100:
            cnt += v // 100
            v = v % 100

        if d == 'L':
            c -= v
            if c < 0 and not zero:
                cnt += 1
        else:
            c += v
            if c > 100 and not zero:
                cnt += 1
        c = c % 100
        zero = 0
        if c == 0:
            cnt += 1
            zero = 1

    return cnt

print(f'Part 1: {part1()}')

print(f'Part 2: {part2()}')
