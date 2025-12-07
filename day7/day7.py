
with open('in.txt') as f:
    data = [list(l.strip()) for l in f.readlines()]

def part1():
    ans = 0
    reachable = set()
    unreachable = set()
    heigth = len(data)
    width = len(data[0])

    def reach(x, y, ogx, ogy):
        if x < 0 or x >= width:
            return 0
        if y < 0 or y >= heigth:
            return 0

        if (x, y) in reachable:
            return 1
        elif (x, y) in unreachable:
            return 0

        if data[y][x] == 'S':
            reachable.add((ogx, ogy))
            return 1

        l = r = 0
        if x > 0 and data[y][x - 1] == '^':
            l = reach(x - 1, y, ogx, ogy)
        if x < width - 1 and data[y][x + 1] == '^':
            r = reach(x + 1, y, ogx, ogy)

        if l or r:
            reachable.add((ogx, ogy))
            return 1
        elif y > 0 and data[y - 1][x] == '^':
            unreachable.add((ogx, ogy))
            return 0

        return reach(x, y - 1, ogx, ogy)

    ans = sum([reach(j, i, j, i) for i in range(len(data)) for j in range(len(data[i])) if data[i][j] == '^'])
    return ans

def part2():
    height = len(data)
    width = len(data[0])

    memo = {}

    def count_timelines(x, y):
        if (x, y) in memo:
            return memo[(x, y)]

        for next_y in range(y + 1, height + 1):
            if next_y == height:
                return 1

            if data[next_y][x] == '^':
                total_paths = 0

                if x - 1 >= 0:
                    total_paths += count_timelines(x - 1, next_y)

                if x + 1 < width:
                    total_paths += count_timelines(x + 1, next_y)

                memo[(x, y)] = total_paths
                return total_paths

        return 0

    start_x = -1
    for x in range(width):
        if data[0][x] == 'S':
            start_x = x
            break

    ans = count_timelines(start_x, 0)

    return ans

print(f'Part 1: {part1()}')

print(f'Part 2: {part2()}')
