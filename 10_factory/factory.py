import re
import time
from itertools import combinations

from z3 import Int, Optimize, Sum, sat

begin = time.time()

###


def parse_lights(line: list[str]) -> tuple[bool]:
    result = []
    for char in line[0][1:]:
        if char == "]":
            continue
        elif char == ".":
            result.append(False)
        elif char == "#":
            result.append(True)
        else:
            raise Exception
    return tuple(result)


def parse_buttons(line: list[str]) -> list[tuple]:
    result = []
    vector_size = len(line[0]) - 2
    for elem in line[1:-1]:
        btn = [int(n) for n in re.findall(r"\d+", elem)]
        btn_vec = tuple(i in btn for i in range(vector_size))
        result.append(btn_vec)
    return result


def parse_joltage(line: list[str]) -> tuple[int]:
    return tuple(int(n) for n in re.findall(r"\d+", line[-1]))


def parse(inp: list[list]) -> tuple:
    lights, buttons, joltage = [], [], []
    for line in inp:
        lights.append(parse_lights(line))
        buttons.append(parse_buttons(line))
        joltage.append(parse_joltage(line))
    return lights, buttons, joltage


def press_light_button(btn: tuple[int], state: tuple[bool]):
    return tuple(not pwr if idx in btn else pwr for idx, pwr in enumerate(state))


def configure_lights(target: tuple[bool], buttons: list[tuple]) -> int:
    initial_state = tuple(False for _ in target)
    for n in range(len(buttons) + 1):
        for comb in combinations(buttons, n):
            state = initial_state
            for btn in comb:
                state = tuple(a != b for a, b in zip(btn, state))
            if state == target:
                return n
    raise Exception


def configure_joltage(target: tuple[int], buttons: list[tuple]) -> int:
    scalars = [Int(f"scalar_{idx}") for idx, _ in enumerate(buttons)]
    optimizer = Optimize()
    for s in scalars:
        optimizer.add(s >= 0)
    for idx, val in enumerate(target):
        weighted_sum = Sum(s * v[idx] for s, v in zip(scalars, buttons))
        optimizer.add(val == weighted_sum)
    optimizer.minimize(Sum(scalars))
    if optimizer.check() != sat:
        raise Exception
    model = optimizer.model()
    return sum(model[s].as_long() for s in scalars)


with open("input.txt") as file:
    manual = [line.strip().split() for line in file.readlines()]

indicator_lights, button_wiring, joltage_reqs = parse(manual)

total = [0, 0]
machine_count = len(indicator_lights)
for i in range(machine_count):
    total[0] += configure_lights(indicator_lights[i], button_wiring[i])
    total[1] += configure_joltage(joltage_reqs[i], button_wiring[i])


print(f"Part 1: {total[0]}")
print(f"Part 2: {total[1]}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
