import re

# Reading input file
f = open("inputs/day09.txt", "r")
lines = f.readlines()

numbers = []

def load_instructions():
    for line in lines:
        numbers.append(int(line.replace("\n", "")))

def has_sum_pair(num, pre_nums):
    for x in pre_nums:
        for y in pre_nums:
            if (x + y) == num:
                return True
    return False

def has_sum_list(num, nums_list):
    result = 0
    for x in nums_list:
        result += x
    return result == num

def part1(preamble):
    index = preamble
    start = 0
    while index < len(numbers):
        num = numbers[index]
        pre_nums = numbers[start:preamble]
        if not has_sum_pair(num, pre_nums):
            return num
        index += 1
        start += 1
        preamble += 1
    return 0

def part2(num):
    end_index = numbers.index(num)
    index = 0
    while index < end_index:
        for x in range(index + 2, end_index + 1):
            nums_list = numbers[index:x]
            if has_sum_list(num, nums_list):
                return min(nums_list) + max(nums_list)
        index += 1
        
load_instructions()

p1 = part1(25)
print(p1)
print(part2(p1))
