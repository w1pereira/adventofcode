# Reading input file
f = open("inputs/day10.txt", "r")
lines = f.readlines()

joltages = []

def load_joltages():
    for line in lines:
        joltages.append(int(line.replace("\n", "")))
    joltages.append(0)
    joltages.append(max(joltages) + 3)
    joltages.sort()

def part1():
    before = 0
    d1 = 0
    d3 = 0
    for num in joltages:
        diff = num - before
        if diff == 1:
            d1 += 1
        elif diff == 3:
            d3 += 1
        before = num
    return d1 * d3

res = {}
def part2(i):
    if i == len(joltages) - 1:
        return 1
    if i in res:
        return res[i]
    ans = 0
    for j in range(i+1, len(joltages)):
        if joltages[j] - joltages[i] <= 3:
             ans += part2(j)
    res[i] = ans
    return ans

load_joltages()
print(part1())
print(part2(0))     
