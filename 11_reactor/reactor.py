import re
import time
from functools import cache

begin = time.time()

###

GRAPH = dict()


@cache
def dfs(current: str, part: int = 1, dac: bool = False, fft: bool = False) -> int:
    total = 0
    for output in GRAPH.get(current, []):
        match part, output:
            case 1, "out": return 1
            case 1, _    : total += dfs(output)
            case 2, "out": return int(dac and fft)
            case 2, "dac": total += dfs(output, part=2, dac=True, fft=fft)
            case 2, "fft": total += dfs(output, part=2, dac=dac, fft=True)
            case 2, _    : total += dfs(output, part=2, dac=dac, fft=fft)
    return total


with open("input.txt") as file:
    for line in file.readlines():
        key, *vals = re.findall(r"\w+", line)
        GRAPH[key] = list(vals)

print(f"Part 1: {dfs("you")}")
print(f"Part 2: {dfs("svr", part=2)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
