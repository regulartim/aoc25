import time

begin = time.time()

###


def find_max_batteries(bank: list, n: int) -> list:
    result = []
    start = 0
    for idx in range(n):
        end = idx + 1 - n
        sub_bank = bank[start:end] if end != 0 else bank[start:]
        result.append(max(sub_bank))
        start = start + sub_bank.index(result[-1]) + 1
    return result


def find_max_joltage(bank: list, n: int) -> int:
    max_batteries = find_max_batteries(bank, n)
    bank_joltage = sum(n * 10**idx for idx, n in enumerate(reversed(max_batteries)))
    return bank_joltage


with open("input.txt") as file:
    battery_banks = [[int(n) for n in list(line.strip())] for line in file]

max_joltages_of_2 = [find_max_joltage(b, 2) for b in battery_banks]
max_joltages_of_12 = [find_max_joltage(b, 12) for b in battery_banks]

print(f"Part 1: {sum(max_joltages_of_2)}")
print(f"Part 2: {sum(max_joltages_of_12)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
