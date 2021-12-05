# Reading input file
f = open("inputs/day01.txt", "r")
lines = f.readlines()
input_numbers = list(map(lambda x: int(x.replace("\n","")), lines))

def part1(numbers):
    last_num = total = 0
    first_line = True
    for number in numbers:
        if first_line:
            first_line = False
        elif number > last_num:
            total += 1
        last_num = number
    return total

def part2():
    numbers = []
    idx = 0
    while idx < len(input_numbers):
        if idx >= 2:
                numbers.append(input_numbers[idx] + input_numbers[idx-1] + input_numbers[idx-2])
        idx += 1
    return part1(numbers)

part1(input_numbers)
part2()