##########
# PART 1 #
##########
scoring = {
    'A': {
        'X': 1 + 3,
        'Y': 2 + 6,
        'Z': 3 + 0,
    },
    'B': {
        'X': 1 + 0,
        'Y': 2 + 3,
        'Z': 3 + 6,
    },
    'C': {
        'X': 1 + 6,
        'Y': 2 + 0,
        'Z': 3 + 3,
    },
}

score = 0
with open('input/day2.txt', 'r') as f:
    for line in f.readlines():
        stripped_line = line.replace('\n', '').strip()
        their_move, your_move = stripped_line.split(' ')
        score += scoring[their_move][your_move]

print(f'DAY 2 PART 1:\n{score}\n')

##########
# PART 2 #
##########
scoring = {
    'A': {
        'X': 3 + 0,
        'Y': 1 + 3,
        'Z': 2 + 6,
    },
    'B': {
        'X': 1 + 0,
        'Y': 2 + 3,
        'Z': 3 + 6,
    },
    'C': {
        'X': 2 + 0,
        'Y': 3 + 3,
        'Z': 1 + 6,
    },
}

score = 0
with open('input/day2.txt', 'r') as f:
    for line in f.readlines():
        stripped_line = line.replace('\n', '').strip()
        their_move, your_move = stripped_line.split(' ')
        score += scoring[their_move][your_move]

print(f'DAY 2 PART 2:\n{score}\n')
