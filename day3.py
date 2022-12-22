##########
# PART 1 #
##########
def priority(c):
    ascii_code = ord(c)
    if ascii_code > 96:
        return ascii_code - 96
    return ascii_code - 38

total_priority = 0

with open('input/day3.txt', 'r') as f:
    for line in f.readlines():
        stripped_line = line.replace('\n', '').strip()
        half_len = len(stripped_line) // 2
        first_half = set()
        for c in stripped_line[:half_len]:
            first_half.add(c)

        second_half = set()
        for c in stripped_line[half_len:]:
            second_half.add(c)

        common_c = list(first_half.intersection(second_half))[0]
        total_priority += priority(common_c)

print(f'DAY 3 PART 1:\n{total_priority}\n')

##########
# PART 2 #
##########
total_priority = 0
first_set = None
second_set = None

with open('input/day3.txt', 'r') as f:
    for line in f.readlines():
        stripped_line = line.replace('\n', '').strip()
        current_set = set()
        for c in stripped_line:
            current_set.add(c)

        if first_set is None:
            first_set = current_set
        elif second_set is None:
            second_set = current_set
        else:
            first_second_common = first_set.intersection(second_set)
            second_third_common = second_set.intersection(current_set)
            common_set = first_second_common.intersection(
                second_third_common)
            common_c = list(common_set)[0]
            total_priority += priority(common_c)
            first_set = None
            second_set = None

print(f'DAY 3 PART 2:\n{total_priority}\n')
