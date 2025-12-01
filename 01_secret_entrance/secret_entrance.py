import time

begin = time.time()

###


def rotate(direction: str, distance: int, position: int) -> tuple[int, int]:
    if direction not in "LR":
        raise ValueError("Invalid direction.")

    zero_passes = distance // 100
    if direction == "L":
        distance = -distance
    new_position = (position + distance) % 100

    zero_passes += direction == "L" and position != 0 and new_position > position
    zero_passes += direction == "R" and new_position != 0 and new_position < position

    return new_position, zero_passes


with open("input.txt") as file:
    instructions = [(line[0], int(line[1:])) for line in file]

position = 50
point_at_zero_count, total_zero_passes = 0, 0
for i in instructions:
    position, zero_passes = rotate(*i, position)
    point_at_zero_count += position == 0
    total_zero_passes += zero_passes

print(f"Part 1: {point_at_zero_count}")
print(f"Part 2: {point_at_zero_count + total_zero_passes}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
