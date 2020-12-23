import re

# Reading input file
f = open("inputs/day08.txt", "r")
lines = f.readlines()

instructions = []

def load_instructions():
    for line in lines:
        instructions.append(re.findall(r"([a-z]+) ([\+|-][0-9]+)", line))

def part1(acc = 0, index = 0, executed = []):
    if index > (len(instructions) - 1) or index in executed: 
        return acc
    i = instructions[index][0]
    executed.append(index)
    if i[0] == "acc":
        acc += int(i[1])
        index += 1
    elif i[0] == "jmp":
        index += int(i[1])
    else:
        index += 1
    return part1(acc, index, executed)

def part2(acc = 0, index = 0, last_jump_index = [], last_jump_acc = [], executed = []):
    if index > (len(instructions) - 1): 
        return acc
    if index in executed:
        index = last_jump_index[-1] + 1
        acc = last_jump_acc[-1]
        return part2(acc, index, last_jump_index[:-1], last_jump_acc[:-1], executed)
    i = instructions[index][0]
    executed.append(index)
    if i[0] == "acc":
        acc += int(i[1])
        index += 1
    elif i[0] == "jmp":
        new_index = index + int(i[1])
        if new_index not in executed:
            last_jump_index.append(index)
            last_jump_acc.append(acc)
        index = new_index
    else:
        index += 1
    return part2(acc, index, last_jump_index, last_jump_acc, executed)

load_instructions()
print(part1())
print(part2())
