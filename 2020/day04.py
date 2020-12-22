import re

# Reading input file
f = open("inputs/day04.txt", "r")
lines = f.readlines()

def valid(input, dict):
    return input in dict

def passport_has_required_fields(p):
    return (
                valid("byr", p) and valid("iyr", p) and valid("eyr", p) and 
                valid("hgt", p) and valid("hcl", p) and valid("ecl", p) and
                valid("pid", p)
            )

def passport_fields_are_valid(p):
    if int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
        return False
    if int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
        return False
    if int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
        return False
    if "cm" not in p["hgt"] and "in" not in p["hgt"]:
        return False
    if "cm" in p["hgt"]:
        value = int(p["hgt"].split("cm")[0])
        if value < 150 or value > 193:
            return False
    if "in" in p["hgt"]:
        value = int(p["hgt"].split("in")[0])
        if value < 59 or value > 76:
            return False 
    if re.search("#[0-9a-f]+", p["hcl"]) is None or len(p["hcl"]) != 7:
        return False
    if re.search("amb|blu|brn|gry|grn|hzl|oth", p["ecl"]) is None or len(p["ecl"]) != 3:
        return False
    if re.search("[0-9]{9}", p["pid"]) is None or len(p["pid"]) != 9:
        return False
    return True
    

def validate_passports(strict_rules = False):
    p = {} # passport
    valid_passports = 0
    for line in lines:
        if line == "\n":
            if (
                passport_has_required_fields(p) and 
                (not strict_rules or passport_fields_are_valid(p))
            ):
                valid_passports += 1
            p = {}
        else:
            line = line.replace("\n", "")
            fields = line.split(" ")
            for field in fields:
                label = field.split(":")[0]
                value = field.split(":")[1]
                p[label] = value
    if (
        passport_has_required_fields(p) and 
        (not strict_rules or passport_fields_are_valid(p))
    ):
        valid_passports += 1
    return valid_passports

print(validate_passports()) # part1
print(validate_passports(True)) # part2