import math
import time
from collections import Counter

begin = time.time()

###


class UnionFind:
    def __init__(self, size: int):
        self.parents = list(range(size))

    def find_representative(self, i: int) -> int:
        if self.parents[i] != i:
            self.parents[i] = self.find_representative(self.parents[i])
        return self.parents[i]

    def union(self, i: int, j: int) -> None:
        i_representative = self.find_representative(i)
        j_representative = self.find_representative(j)
        self.parents[i_representative] = j_representative

    def is_uniform(self) -> bool:
        first = self.find_representative(0)
        return all(first == self.find_representative(i) for i in range(len(self.parents)))


def product(numbers: list[int]) -> int:
    acc = 1
    for n in numbers:
        acc *= n
    return acc


def get_distances(boxes: list[tuple]) -> list[tuple]:
    result = []
    for i, a in enumerate(boxes):
        for j, b in enumerate(boxes[i + 1 :]):
            result.append((math.dist(a, b), i, j + i + 1))
    return result


def circuit_sizes_after(n: int, box_count: int, dists: list[tuple]) -> Counter:
    u = UnionFind(box_count)
    for _, i, j in dists[:n]:
        u.union(i, j)
    return Counter([u.find_representative(i) for i in range(box_count)])


def last_connection(box_count: int, dists: list[tuple]) -> tuple[int]:
    u = UnionFind(box_count)
    for _, i, j in dists:
        u.union(i, j)
        if u.is_uniform():
            return (i, j)
    return (-1, -1)


with open("input.txt") as file:
    junction_boxes = [tuple(int(n) for n in line.split(",")) for line in file.readlines()]

distances = get_distances(junction_boxes)
distances.sort()
circuits = circuit_sizes_after(1000, len(junction_boxes), distances)
last_a, last_b = last_connection(len(junction_boxes), distances)


print(f"Part 1: {product(count for _, count in circuits.most_common(3))}")
print(f"Part 2: {junction_boxes[last_a][0] * junction_boxes[last_b][0]}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
