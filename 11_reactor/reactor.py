import re
import time

begin = time.time()

###

CACHE = dict()

def dfs(wires, current, part2=False, dac=False, fft=False) -> int:
    state = (current, dac, fft, part2) 
    if state in CACHE:
        return CACHE[state]
    total = 0
    for output in wires[current]:
        if not part2:
            if output == "out":
                return 1
            total += dfs(wires, output)
            continue
        match output:
            case "out": return int(dac and fft)
            case "dac": total += dfs(wires, output, part2, dac=True, fft=fft)
            case "fft": total += dfs(wires, output, part2, dac=dac, fft=True)
            case _    : total += dfs(wires, output, part2, dac=dac, fft=fft)
    CACHE[state] = total
    return total


wiring = dict()
with open("input.txt") as file:
    for line in file.readlines():
        key, *vals = re.findall(r"\w+", line)
        wiring[key] = list(vals)

print(f"Part 1: {dfs(wiring, "you")}")
print(f"Part 2: {dfs(wiring, "svr", part2=True)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
