# Reading input file
f = open("inputs/day02.txt", "r")
lines = f.readlines()

def part1():
    valid_passwords = 0
    for line in lines:
        password = line.replace("\n", "").split(": ")
        min_occurrence = int(password[0].split(" ")[0].split("-")[0])
        max_occurrence = int(password[0].split(" ")[0].split("-")[1])
        letter = password[0].split(" ")[1]
        count = password[1].count(letter)
        if count >= min_occurrence and count <= max_occurrence:
            valid_passwords += 1
    return valid_passwords

def part2():
    valid_passwords = 0
    for line in lines:
        password = line.replace("\n", "").split(": ")
        first_occurrence = int(password[0].split(" ")[0].split("-")[0])
        second_occurrence = int(password[0].split(" ")[0].split("-")[1])
        letter = password[0].split(" ")[1]
        first_valid = password[1][first_occurrence-1] == letter
        second_valid = password[1][second_occurrence-1] == letter
        if (first_valid and not second_valid) or (not first_valid and second_valid):
             valid_passwords += 1
    return valid_passwords

print(part1())
print(part2())