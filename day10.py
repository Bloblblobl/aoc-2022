##########
# PART 1 #
##########
lines = []
with open('input/day10.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', ''))

signal_strengths = 0
first_cycle = 20
cycle_interval = 40
cycle_checks = 6
last_cycle = first_cycle + cycle_interval * (cycle_checks - 1)
cycle = 0
register = 1
line_count = 0

def check_cycle():
    global cycle
    global register
    global signal_strengths
    global line_count
    cycle += 1

    if cycle < first_cycle:
        return
    
    if (cycle - first_cycle) % cycle_interval == 0:
        signal_strengths += cycle * register

while len(lines) and cycle <= last_cycle:
    next_line = lines.pop(0)
    line_count += 1
    if next_line == 'noop':
        check_cycle()
    else:
        check_cycle()
        check_cycle()
        register += int(next_line.split(' ')[1])

print(f'DAY 10 PART 1:\n{signal_strengths}\n')
