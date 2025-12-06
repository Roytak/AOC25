
def part1():
    ans = []
    ops = []
    with open('in.txt') as f:
        for line in f.readlines():
            data = " ".join(line.strip().split())
            data = data.split(' ')
            if ans == []:
                ans = [[0, 1] for _ in range(len(data))]
            i = 0
            for d in data:
                if d == '*' or d == '+':
                    ops.append(d)
                else:
                    ans[i][0] += int(d)
                    ans[i][1] *= int(d)
                i += 1
    res = 0
    for i in range(len(ops)):
        res += ans[i][0] if ops[i] == '+' else ans[i][1]

    return res

def part2():
    with open('in.txt') as f:
        map = f.read().split('\n')
        ops = " ".join(map[-1].split()).split(' ')
        map = map[:-1]
    maxlen = max([len(line) for line in map])
    for i in range(len(map)):
        map[i] = map[i] + ' ' * (maxlen - len(map[i]))

    res = [0 if op == '+' else 1 for op in ops]

    idx = 0
    for col in range(maxlen):
        numc = 0
        for l in map:
            if l[col] != ' ':
                numc += 1

        if numc == 0:
            idx += 1
            continue

        dig = 0
        for l in map:
            if l[col] != ' ':
                dig += int(l[col]) * pow(10, numc - 1)
                numc -= 1

        if ops[idx] == '+':
            res[idx] += dig
        else:
            res[idx] *= dig

    return sum(res)

print(f'Part 1: {part1()}')

print(f'Part 2: {part2()}')
