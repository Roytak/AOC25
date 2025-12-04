
with open('/home/roman/AOC25/day4/in.txt') as f:
    data = [line.strip() for line in f.readlines()]

def part1():
    ans = 0

    def check(x, y):
        nbrs = 0
        heigth = len(data)
        width = len(data[0])
        # t
        if y - 1 >= 0:
            if data[y - 1][x] == '@':
                nbrs += 1
            # tr
            if x + 1 < width:
                if data[y - 1][x + 1] == '@':
                    nbrs += 1
        # r
        if x + 1 < width:
            if data[y][x + 1] == '@':
                nbrs += 1
            # br
            if y + 1 < heigth:
                if data[y + 1][x + 1] == '@':
                    nbrs += 1
        # b
        if y + 1 < heigth:
            if data[y + 1][x] == '@':
                nbrs += 1
            # bl
            if x - 1 >= 0:
                if data[y + 1][x - 1] == '@':
                    nbrs += 1
        # l
        if x - 1 >= 0:
            if data[y][x - 1] == '@':
                nbrs += 1
            # tl
            if y - 1 >= 0:
                if data[y - 1][x - 1] == '@':
                    nbrs += 1

        return 1 if nbrs < 4 else 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '@':
                ans += check(j, i)

    return ans

def part2():
    ans = 0

    global data
    data = [list(line) for line in data]
    heigth = len(data)
    width = len(data[0])

    def check(x, y):
        nbrs = 0
        nbr_coords = [
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]

        for dy, dx in nbr_coords:
            nx, ny = x + dx, y + dy

            if 0 <= nx < width and 0 <= ny < heigth and data[ny][nx] == '@':
                nbrs += 1

        return 1 if nbrs < 4 else 0

    while True:
        to_del = [
            (i, j)
            for i in range(heigth)
            for j in range(width)
            if data[i][j] == '@' and check(j, i)
        ]

        found = len(to_del)
        if not found:
            break

        ans += found

        for y, x in to_del:
            data[y][x] = '.'

    return ans

print(f'Part 1: {part1()}')

print(f'Part 2: {part2()}')
