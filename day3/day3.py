
with open('in.txt') as f:
    data = [line.strip() for line in f.readlines()]


def part1():
    ans = 0

    for line in data:
        a = 0
        for i in range(9, 0, -1):
            for j in range(len(line) - 1):
                if i == int(line[j]):
                    a = 10 * int(line[j])
                    break
            if a:
                break
        mx = max(int(x) for x in line[j + 1:])
        ans += a + mx

    return ans

def part2():
    ans = 0

    for line in data:
        tmp = 0
        new_start = -1
        for b in range(0, 12):
            max = 0
            l = len(line) - 12 + b + 1
            for i in range(new_start + 1, l):
                if int(line[i]) > max:
                    max = int(line[i])
                    new_start = i
            tmp += max * pow(10, 12 - b - 1)
        ans += tmp

    return ans

print(f'Part 1: {part1()}')

print(f'Part 2: {part2()}')
