import time

begin = time.time()

###


def is_fresh(ing_id: int, ranges: list[tuple]) -> bool:
    for start, end in ranges:
        if ing_id < start:
            return False
        if ing_id <= end:
            return True
    return False


def merge_overlapping_ranges(r: tuple, s: tuple) -> tuple:
    return (min([r[0], s[0]]), max([r[1], s[1]]))


def collapse_range_list(ranges: list[tuple]) -> list[tuple]:
    result = [ranges[0]]
    for idx, s in enumerate(ranges[1:]):
        r = result[-1]
        if r[1] < s[0]:
            result.append(s)
        else:
            result[-1] = merge_overlapping_ranges(r, s)
    return result


def count_ids_in_ranges(ranges: list[tuple]) -> int:
    result = 0
    for start, end in collapse_range_list(ranges):
        result += 1 + end - start
    return result


with open("input.txt") as file:
    blocks = [b.split() for b in file.read().strip().split("\n\n")]

id_ranges = [tuple(int(n) for n in line.split("-")) for line in blocks[0]]
id_ranges.sort()
ingredient_ids = [int(line) for line in blocks[1]]

fresh_ids = [i for i in ingredient_ids if is_fresh(i, id_ranges)]

print(f"Part 1: {len(fresh_ids)}")
print(f"Part 2: {count_ids_in_ranges(id_ranges)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
