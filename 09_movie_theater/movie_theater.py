import time

begin = time.time()

###


def area(a: tuple[int], b: tuple[int]) -> int:
    return (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1]))


def intersecting(line1: tuple[int], line2: tuple[int]) -> bool:
    p, q, r, s = *line1, *line2
    line1_horizontal = p[1] == q[1]
    line2_horizontal = r[1] == s[1]
    if line1_horizontal == line2_horizontal:
        return False
    if line1_horizontal:
        assert r[0] == s[0]
        return min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and min(r[1], s[1]) <= p[1] <= max(r[1], s[1])
    else:
        assert r[1] == s[1]
        return min(p[1], q[1]) <= r[1] <= max(p[1], q[1]) and min(r[0], s[0]) <= p[0] <= max(r[0], s[0])


def is_valid_rectangle(a: tuple, b: tuple, edges: list[tuple]) -> bool:
    ax, ay, bx, by = *a, *b
    if ax == bx or ay == by:
        return False
    if ax > bx:
        return False
    ax += 1
    bx -= 1
    if ay < by:
        ay += 1
        by -= 1
    else:
        ay -= 1
        by += 1
    rectangle = [((ax, ay), (ax, by)), ((ax, by), (bx, by)), ((bx, by), (bx, ay)), ((bx, ay), (ax, ay))]
    return not any(intersecting(redge, pedge) for redge in rectangle for pedge in edges)


def max_area(corners: list[tuple], edges: list[tuple]) -> int:
    for pair in corners:
        if is_valid_rectangle(*pair, edges):
            return area(*pair)
    return -1


with open("input.txt") as file:
    red_tiles = [tuple(int(n) for n in line.split(",")) for line in file.readlines()]

polygon_edges = list(zip(red_tiles, red_tiles[1:])) + [(red_tiles[-1], red_tiles[0])]
polygon_edges.sort(key=lambda e: abs(e[0][0] - e[1][0]) + abs(e[0][1] - e[1][1]), reverse=True)

corner_pairs = [(tile_a, tile_b) for idx, tile_a in enumerate(red_tiles) for tile_b in red_tiles[idx + 1 :]]
corner_pairs.sort(key=lambda pair: area(*pair), reverse=True)

print(f"Part 1: {area(*corner_pairs[0])}")
print(f"Part 2: {max_area(corner_pairs, polygon_edges)}")


###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
