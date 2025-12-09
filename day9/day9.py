
with open('in.txt') as f:
    data = [tuple(map(int, line.strip().split(','))) for line in f]

def part1():
    return max(map(max, [[(abs(x2 - x1) + 1) * (abs(y2 - y1) + 1) for x2, y2 in data] for x1, y1 in data]))

def part2():
    edges = []
    for i in range(len(data) - 1):
        edges.append((data[i], data[i + 1]))
    edges.append((data[-1], data[0]))

    def is_valid_rect(rect_min_x, rect_max_x, rect_min_y, rect_max_y):
        for (x1, y1), (x2, y2) in edges:
            if x1 == x2:
                if rect_min_x < x1 < rect_max_x:
                    edge_min_y = min(y1, y2)
                    edge_max_y = max(y1, y2)
                    overlap_min = max(edge_min_y, rect_min_y)
                    overlap_max = min(edge_max_y, rect_max_y)
                    if overlap_min < overlap_max:
                        return False
            else:
                if rect_min_y < y1 < rect_max_y:
                    edge_min_x = min(x1, x2)
                    edge_max_x = max(x1, x2)
                    overlap_min = max(edge_min_x, rect_min_x)
                    overlap_max = min(edge_max_x, rect_max_x)
                    if overlap_min < overlap_max:
                        return False
        return True

    mapped_areas = {}
    for i in range(len(data)):
        x1, y1 = data[i]
        for j in range(len(data)):
            x2, y2 = data[j]
            a = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if a > 1:
                mapped_areas[(x1, y1, x2, y2)] = a

    sorted_areas = sorted(mapped_areas.items(), key=lambda item: item[1], reverse=True)
    for (x1, y1, x2, y2), area in sorted_areas:
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        if is_valid_rect(min_x, max_x, min_y, max_y):
            return area
    return 0

print(f'Part 1: {part1()}')

print(f'Part 2: {part2()}')
