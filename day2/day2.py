
data = []

with open('in.txt') as f:
    data = f.read().split(',')

def part1():
    ans = 0

    def check(str):
        ok = 1
        i = 0

        if len(str) % 2 == 1:
            return 0

        j = len(str) // 2
        for i in range(len(str) // 2):
            if str[i] != str[j]:
                ok = 0
                break
            j += 1

        if ok:
            return int(str)
        return 0

    for d in data:
        spl = d.split('-')
        min = int(spl[0])
        max = int(spl[1])
        for i in range(min, max + 1):
            ans += check(str(i))

    return ans


def part2():
    ans = 0

    def check(str, substr_len):
        ok = 1

        if len(str) % substr_len != 0:
            return 0

        orig_substr = str[:substr_len]
        for i in range(len(str) // substr_len):
            if str[i * substr_len : i * substr_len + substr_len] != orig_substr:
                ok = 0

        if ok:
            return int(str)
        return 0

    for d in data:
        spl = d.split('-')
        min = int(spl[0])
        max = int(spl[1])
        for i in range(min, max + 1):
            r = 0
            for j in range(len(str(i)) // 2):
                r = check(str(i), j + 1)
                if r:
                    ans += r
                    break

    return ans

# print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
