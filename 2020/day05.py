# Reading input file
f = open("inputs/day05.txt", "r")
lines = f.readlines()

def get_position(low, high, seat_code, lower_label):
    if high - low == 2:
        if len(seat_code) == 1:
            if seat_code == lower_label:
                return low
            else:
                return high - 1
        else:
            return 0
    else:
        if seat_code[0] == lower_label:
            return get_position(low, ((high - low) / 2) + low, seat_code[1:], lower_label)
        else:
            return get_position(((high - low) / 2) + low, high, seat_code[1:], lower_label)
        
def get_seat_id(seat_code):
    row = get_position(0, 128, seat_code[:7], "F")
    column = get_position(0, 8, seat_code[7:], "L")
    return int((row * 8) + column)

def part1():
    highest_seat_id = 0
    for seat_code in lines:
        seat_code = seat_code.replace("\n", "")
        seat_id = get_seat_id(seat_code)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    return highest_seat_id

def part2():
    seats = []
    for seat_code in lines:
        seat_code = seat_code.replace("\n", "")
        seat_id = get_seat_id(seat_code)
        seats.append(seat_id)
    seats.sort()
    low = seats[0]
    high = seats[len(seats)-1]
    for num in range(low, high, +1):
        if num not in seats:
            return num
    return 0

print(part1())
print(part2())