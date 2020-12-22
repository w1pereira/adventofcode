# Reading input file
f = open("inputs/day03.txt", "r")
lines = f.readlines()

def part1(x_distance, y_distance):
    trees = 0
    x_position = 0
    y_position = 1
    for line in lines:
        line = line.replace("\n", "")
        if x_position == 0:
            x_position += x_distance
        elif (y_position % y_distance == 1) or y_distance == 1:
            length = len(line)
            if x_position > (length - 1):
                x_position = x_position % length
            if line[x_position] == "#":
                trees += 1
            x_position += x_distance
        y_position += 1
    return trees

def part2():
    r1_d1 = part1(1, 1)
    r3_d1 = part1(3, 1)
    r5_d1 = part1(5, 1)
    r7_d1 = part1(7, 1)
    r1_d2 = part1(1, 2)
    return r1_d1 *  r3_d1 * r5_d1 * r7_d1 * r1_d2
    
print(part1(3, 1))
print(part2())