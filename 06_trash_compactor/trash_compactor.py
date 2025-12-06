import time

begin = time.time()

###


def product(numbers: list[int]) -> int:
    acc = 1
    for n in numbers:
        acc *= n
    return acc


def parse_p1_problems(lines: list[str]) -> list[str]:
    rows = [line.split() for line in lines]
    return list(zip(*rows))


def parse_p2_problems(lines: list[str]) -> list[str]:
    rows = [list(line) for line in lines]
    problems = []
    for col in zip(*rows):
        op = col[-1].strip()
        if op:
            problems.append([op])
        num = "".join(col[:-1]).strip()
        if num:
            problems[-1].append(num)
    return [problem[::-1] for problem in problems]


def get_total(problems: list[str]) -> int:
    total = 0
    for *ns, op in problems:
        ns = [int(n) for n in ns]
        total += sum(ns) if op == "+" else product(ns)
    return total


with open("input.txt") as file:
    lines = list(file.readlines())

p1_problems = parse_p1_problems(lines)
p2_problems = parse_p2_problems(lines)

print(f"Part 1: {get_total(p1_problems)}")
print(f"Part 2: {get_total(p2_problems)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
