import time

begin = time.time()

###


def area(a: tuple[int], b: tuple[int]) -> int:
    return (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1]))


def max_area1(tiles: list[tuple]) -> int:
    result = 0
    for idx, tile_a in enumerate(tiles):
        for tile_b in red_tiles[idx:]:
            result = max(result, area(tile_a, tile_b))
    return result


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


def max_area2(tiles: list[tuple], edges: list[tuple]) -> int:
    result = 0
    for tile_a in red_tiles:
        for tile_b in red_tiles:
            ax, ay, bx, by = *tile_a, *tile_b
            if ax == bx or ay == by:
                continue
            if ax > bx:
                continue
            ax += 1
            bx -= 1
            if ay < by:
                ay += 1
                by -= 1
            else:
                ay -= 1
                by += 1
            rectangle = [((ax, ay), (ax, by)), ((ax, by), (bx, by)), ((bx, by), (bx, ay)), ((bx, ay), (ax, ay))]
            if any(intersecting(redge, pedge) for redge in rectangle for pedge in edges):
                continue
            result = max(result, area(tile_a, tile_b))
    return result


with open("input.txt") as file:
    red_tiles = [tuple(int(n) for n in line.split(",")) for line in file.readlines()]
edges = list(zip(red_tiles, red_tiles[1:])) + [(red_tiles[-1], red_tiles[0])]

print(f"Part 1: {max_area1(red_tiles)}")
print(f"Part 2: {max_area2(red_tiles, edges)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
