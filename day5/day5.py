
with open('in.txt') as f:
    in_ranges, in_ids = f.read().strip().split('\n\n')

    ranges = [
        (int(s), int(e))
        for line in in_ranges.split('\n')
        for s, e in [line.split('-')]
    ]

    ids = [
        int(i) for i in in_ids.split('\n')
    ]

def part1():
    ans = 0

    for i in ids:
        for rmin, rmax in ranges:
            if rmin <= i <= rmax:
                ans += 1
                break
    return ans

def part2():
    ans = 0
    new_ranges = []

    # remove all duplicate ranges
    global ranges
    ranges = list(set(ranges))

    while len(ranges) > 0:
        orig_minr = minr = min(mi for mi, _ in ranges)
        orig_maxr = maxr = max(ma for _, ma in ranges)
        for mi, ma in ranges:
            if mi == minr:
                if ma <= maxr:
                    orig_maxr = maxr = ma

        while True:
            orig_len = len(ranges)
            for mi, ma in ranges:
                if minr <= mi <= maxr and (mi != orig_minr or ma != orig_maxr):
                    maxr = max(maxr, ma)
                    ranges.remove((mi, ma))
            new_len = len(ranges)
            if orig_len == new_len:
                break

        new_ranges.append((minr, maxr))
        ranges.remove((orig_minr, orig_maxr))

    for rmin, rmax in new_ranges:
        ans += rmax - rmin + 1
    return ans

print(f'Part 1: {part1()}')

print(f'Part 2: {part2()}')
