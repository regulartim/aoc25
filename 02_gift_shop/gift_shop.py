import re
import time

begin = time.time()

###

P1_PATTERN = re.compile(r"(\d+)\1")
P2_PATTERN = re.compile(r"(\d+)\1+")


def is_invalid(product_id: int, part2: bool = False) -> bool:
    id_str = str(product_id)
    pattern = P2_PATTERN if part2 else P1_PATTERN
    return bool(pattern.fullmatch(id_str))


with open("input.txt") as file:
    id_ranges = [pair.split("-") for pair in file.read().strip().split(",")]

ids = [i for r in id_ranges for i in r]
invalid_ids_p1 = [i for start, end in id_ranges for i in range(int(start), int(end) + 1) if is_invalid(i)]
invalid_ids_p2 = [i for start, end in id_ranges for i in range(int(start), int(end) + 1) if is_invalid(i, True)]

print(f"Part 1: {sum(invalid_ids_p1)}")
print(f"Part 2: {sum(invalid_ids_p2)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
