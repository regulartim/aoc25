import re
import time

begin = time.time()

###


def can_fit_presents(region: tuple, presents: list) -> bool:
    width, length, qty = region
    total_qty = sum(qty)
    if (width // 3) * (length // 3) >= total_qty:
        return True
    tile_counts = [sum(row.count("#") for row in p) for p in presents]
    total_tiles = sum(qty[idx] * c for idx, c in enumerate(tile_counts))
    if total_tiles > width * length:
        return False
    raise Exception


with open("input.txt") as file:
    sections = file.read().strip().split("\n\n")

present_shapes = []
for sec in sections[:-1]:
    shape = [list(line.strip()) for line in sec.split("\n") if ":" not in line]
    present_shapes.append(shape)

regions = []
for line in sections[-1].split("\n"):
    ns = [int(n) for n in re.findall(r"\d+", line)]
    width, length, *qty = ns
    regions.append((width, length, qty))

results = [can_fit_presents(r, present_shapes) for r in regions]
print(f"Part 1: {sum(results)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
