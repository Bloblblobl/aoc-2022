##########
# PART 1 #
##########
current_max = 0
current_count = 0
with open('input/day1.txt', 'r') as f:
    for line in f.readlines():
        stripped_line = line.replace('\n', '')
        if not stripped_line:
            if current_count > current_max:
                current_max = current_count
            current_count = 0
        else:
            current_count += int(stripped_line)

    if current_count > current_max:
        current_max = current_count
    else:
        current_max = current_max

print(f'DAY 1 PART 1:\n{current_max}\n')

##########
# PART 2 #
##########
current_maxes = [0, 0, 0]
current_count = 0

def update_maxes(current_maxes, new_value):
    if new_value > current_maxes[0]:
        current_maxes[1] = current_maxes[0]
        current_maxes[2] = current_maxes[1]
        current_maxes[0] = new_value
    elif new_value > current_maxes[1]:
        current_maxes[2] = current_maxes[1]
        current_maxes[1] = new_value
    elif new_value > current_maxes[2]:
        current_maxes[2] = new_value

with open('input/day1.txt', 'r') as f:
    for line in f.readlines():
        stripped_line = line.replace('\n', '')
        if not stripped_line:
            update_maxes(current_maxes, current_count)
            current_count = 0
        else:
            current_count += int(stripped_line)

    update_maxes(current_maxes, current_count)

print(f'DAY 1 PART 2:\n{sum(current_maxes)}\n')
