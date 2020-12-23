import re

# Reading input file
f = open("inputs/day07.txt", "r")
lines = f.readlines()

bag_colors = {}
bag_colors_can_contain = []

def load_bag_colors():
    for line in lines:
        line = line.replace("\n", "")
        bg = line.split(" bags contain ")[0]
        bg_contain = line.split(" bags contain ")[1]
        bag_colors[bg] = re.findall("([0-9]) ([a-z ]+) bag", bg_contain)

def load_bag_colors_can_contain(color, bag_colors):
    for bg in bag_colors:
        for item in bag_colors[bg]:
            if color == item[1]:
                if bg not in bag_colors_can_contain:
                    bag_colors_can_contain.append(bg)
                    load_bag_colors_can_contain(bg, bag_colors)

def get_total_bags_by_color(color, bag_colors, total = 1):
    total_bags = 0
    for bg in bag_colors:
        if color == bg:
            for item in bag_colors[bg]:
                tb = 0
                tb += int(item[0]) * total
                tb += get_total_bags_by_color(item[1], bag_colors, tb)
                total_bags += tb
    return total_bags

load_bag_colors()

# part 1
load_bag_colors_can_contain("shiny gold", bag_colors)
print(len(bag_colors_can_contain))

# part 2
print(get_total_bags_by_color("shiny gold", bag_colors)) 
