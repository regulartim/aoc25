import time

begin = time.time()

###

SEEN = dict()
SPLITTERS = set()


def count_splits(current: tuple[int], end: int, part2: bool = False) -> int:
    while current[1] <= end:
        if current in SPLITTERS:
            if current in SEEN:
                return SEEN[current] if part2 else 0
            left = (current[0] - 1, current[1])
            right = (current[0] + 1, current[1])
            SEEN[current] = 1 + count_splits(left, end, part2) + count_splits(right, end, part2)
            return SEEN[current]
        else:
            current = (current[0], current[1] + 1)
    return 0


source = (0, 0)
with open("input.txt") as file:
    for y, line in enumerate(file.readlines()):
        for x, char in enumerate(line):
            if char == "S":
                source = (x, y)
            if char == "^":
                SPLITTERS.add((x, y))
    max_y = y

split_count = count_splits(source, max_y)
SEEN.clear()
timeline_count = 1 + count_splits(source, max_y, part2=True)

print(f"Part 1: {split_count}")
print(f"Part 2: {timeline_count}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
