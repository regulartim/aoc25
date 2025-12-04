import time

begin = time.time()

###

ADJACENCY = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def part_1(grid: set) -> int:
    access_count = 0
    for roll in grid:
        neighbour_count = 0
        for delta in ADJACENCY:
            neighbour = add_tuples(roll, delta)
            neighbour_count += neighbour in grid
        access_count += neighbour_count < 4
    return access_count


def part_2(grid: set) -> int:
    to_check = grid.copy()
    access_count = 0
    while to_check:
        roll = to_check.pop()
        neighbours = [add_tuples(roll, delta) for delta in ADJACENCY]
        neighbours = [n for n in neighbours if n in grid]
        if len(neighbours) < 4:
            grid.remove(roll)
            to_check.update(neighbours)
            access_count += 1
    return access_count


roll_grid = set()
with open("input.txt") as file:
    for y, line in enumerate(file.readlines()):
        for x, char in enumerate(line):
            if char == "@":
                roll_grid.add((x, y))

print(f"Part 1: {part_1(roll_grid)}")
print(f"Part 2: {part_2(roll_grid)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
