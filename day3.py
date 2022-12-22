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
