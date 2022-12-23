##########
# PART 1 #
##########
with open('input/day6.txt', 'r') as f:
    last_4_seen = []
    input = f.readlines()[0].replace('\n', '')
    for i, c in enumerate(input):
        last_4_seen.append(c)
        if len(last_4_seen) > 4:
            last_4_seen.pop(0)

        if len(last_4_seen) == 4 and len(last_4_seen) == len(set(last_4_seen)):
            marker_index = i + 1
            break

    print(f'DAY 6 PART 1:\n{marker_index}\n')