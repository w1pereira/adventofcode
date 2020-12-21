# Reading input file
f = open("inputs/day01.txt", "r")
lines = f.readlines()
input_numbers = list(map(lambda x: int(x.replace("\n","")), lines))

# Finding two numbers that sum to and multiplying them
def part1(sum_to):
    for first_number in input_numbers:
        second_number = sum_to - first_number
        if second_number in input_numbers:
            return (first_number * second_number)
    return 0

# Finding three numbers that sum to and multiplying them
def part2(sum_to):
    for first_number in input_numbers:
        other_numbers_added_up = sum_to - first_number
        first_result = part1(other_numbers_added_up)
        if first_result != 0:
            return (first_number * first_result)
    return 0
            
print(part1(2020))
print(part2(2020))