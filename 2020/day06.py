# Reading input file
f = open("inputs/day06.txt", "r")
lines = f.readlines()

def get_answers_count(answers):
    distinct = list(set(answers))
    return len(distinct)

def get_everyone_answers_count(answers, people_count):
    ans_count = {}
    everyone_answers = 0
    for a in answers:
        if a not in ans_count:
            ans_count[a] = 1
        else:
            ans_count[a] += 1
    for a in ans_count:
        if ans_count[a] == people_count:
            everyone_answers += 1
    return everyone_answers

def get_total_answers_count(everyone = False):
    answers = []
    people_count = 0
    sum_of_counts = 0
    for line in lines:
        if line == "\n":
            if not everyone:
                sum_of_counts += get_answers_count(answers)  
            else:
                sum_of_counts += get_everyone_answers_count(answers, people_count)
            answers = []
            people_count = 0
        else:
            people_count += 1
            line = line.replace("\n", "")
            for char in line:
                answers.append(char)
    if not everyone:
        sum_of_counts += get_answers_count(answers)  
    else:
        sum_of_counts += get_everyone_answers_count(answers, people_count)
    return sum_of_counts
            
print(get_total_answers_count()) # part1
print(get_total_answers_count(True)) # part2