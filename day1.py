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
