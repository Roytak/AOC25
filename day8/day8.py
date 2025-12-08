from math import sqrt

NUM_ITERS = 1000

with open('in.txt') as f:
    data_in = [l.strip() for l in f.readlines()]
    data = []
    for line in data_in:
        x, y, z = map(int, line.split(','))
        data.append((x, y, z))

def part1():
    distances = []
    circuits = []

    for line in data:
        x, y, z = line
        c = [(x, y, z)]
        circuits.append(c)

        dist = []
        for l2 in data:
            x2, y2, z2 = l2
            dx = pow(x2 - x, 2)
            dy = pow(y2 - y, 2)
            dz = pow(z2 - z, 2)
            dist.append(sqrt(dx + dy + dz))
        mx = max(dist)
        for i, d in enumerate(dist):
            if d == 0.00:
                # to never select this
                dist[i] = mx + 1
        distances.append(dist)

    for i in range(NUM_ITERS):
        mins = [min(d) for d in distances]
        mi = max(mins)
        idx = 0
        for j in range(len(mins)):
            if mins[j] < mi:
                mi = mins[j]
                idx = j
        jb1 = data[idx]

        for j in range(len(distances[idx])):
            if distances[idx][j] == mi:
                jb2 = data[j]
                idx2 = j
                break

        # find the circuit of jb1 and jb2
        for c in circuits:
            if jb1 in c:
                c1 = c
            if jb2 in c:
                c2 = c
        if c1 != c2:
            for c in c2:
                if c not in c1:
                    c1.append(c)
            circuits.remove(c2)

        distances[idx][idx2] = mx + 1
        distances[idx2][idx] = mx + 1

    mxc = [len(c) for c in circuits]
    mxc.sort(reverse=True)
    return mxc[0] * mxc[1] * mxc[2]

def part2():
    distances = []
    circuits = []

    for line in data:
        x, y, z = line
        c = [(x, y, z)]
        circuits.append(c)

        dist = []
        for l2 in data:
            x2, y2, z2 = l2
            dx = pow(x2 - x, 2)
            dy = pow(y2 - y, 2)
            dz = pow(z2 - z, 2)
            dist.append(sqrt(dx + dy + dz))
        mx = max(dist)
        for i, d in enumerate(dist):
            if d == 0.00:
                # to never select this
                dist[i] = mx + 1
        distances.append(dist)

    while True:
        mins = [min(d) for d in distances]
        mi = max(mins)
        idx = 0
        for j in range(len(mins)):
            if mins[j] < mi:
                mi = mins[j]
                idx = j
        jb1 = data[idx]

        for j in range(len(distances[idx])):
            if distances[idx][j] == mi:
                jb2 = data[j]
                idx2 = j
                break

        # find the circuit of jb1 and jb2
        for c in circuits:
            if jb1 in c:
                c1 = c
            if jb2 in c:
                c2 = c
        if c1 != c2:
            for c in c2:
                if c not in c1:
                    c1.append(c)
            circuits.remove(c2)

        if len(circuits) == 1:
            return jb1[0] * jb2[0]

        distances[idx][idx2] = mx + 1
        distances[idx2][idx] = mx + 1

print(f'Part 1: {part1()}')

print(f'Part 2: {part2()}')
