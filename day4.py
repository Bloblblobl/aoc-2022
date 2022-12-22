##########
# PART 1 #
##########
fully_encompassed_ranges = 0

with open('input/day4.txt', 'r') as f:
    for line in f.readlines():
        stripped_line = line.replace('\n', '').strip()
        first_sections, second_sections = stripped_line.split(',')
        first_start, first_end = first_sections.split('-')
        second_start, second_end = second_sections.split('-')
        first_encompasses_second = int(first_start) <= int(
            second_start) and int(first_end) >= int(second_end)
        second_encompasses_first = int(first_start) >= int(
            second_start) and int(first_end) <= int(second_end)
        if first_encompasses_second or second_encompasses_first:
            fully_encompassed_ranges += 1

print(f'DAY 4 PART 1:\n{fully_encompassed_ranges}\n')

##########
# PART 2 #
##########
overlapping_ranges = 0

with open('input/day4.txt', 'r') as f:
    for line in f.readlines():
        stripped_line = line.replace('\n', '').strip()
        first_sections, second_sections = stripped_line.split(',')
        first_start, first_end = first_sections.split('-')
        second_start, second_end = second_sections.split('-')
        first_overlapping_second = int(first_start) <= int(
            second_start) and int(first_end) >= int(second_start)
        second_overlapping_first = int(first_start) >= int(
            second_start) and int(second_end) >= int(first_start)
        if first_overlapping_second or second_overlapping_first:
            overlapping_ranges += 1

print(f'DAY 4 PART 2:\n{overlapping_ranges}\n')
