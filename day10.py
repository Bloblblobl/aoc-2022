##########
# PART 1 #
##########
lines = []
with open('input/day10.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', ''))

lines2 = lines.copy()

signal_strengths = 0
first_cycle = 20
cycle_interval = 40
cycle_checks = 6
last_cycle = first_cycle + cycle_interval * (cycle_checks - 1)
cycle = 0
register = 1

def check_cycle():
    global cycle
    global register
    global signal_strengths
    cycle += 1

    if cycle < first_cycle:
        return
    
    if (cycle - first_cycle) % cycle_interval == 0:
        signal_strengths += cycle * register

while len(lines) and cycle <= last_cycle:
    next_line = lines.pop(0)
    if next_line == 'noop':
        check_cycle()
    else:
        check_cycle()
        check_cycle()
        register += int(next_line.split(' ')[1])

print(f'DAY 10 PART 1:\n{signal_strengths}\n')

##########
# PART 2 #
##########
cycle = 0
register = 1
render = ['']
render_index = 0

def render_cycle():
    global cycle
    global render_index
    cycle += 1

    if cycle > 1 and (cycle - 1) % cycle_interval == 0:
        render_index += 1
        render.append('')
    
    if abs(register - (cycle % cycle_interval) + 1) <= 1:
        render[render_index] += '#'
    else:
        render[render_index] += '.'


while len(lines2):
    next_line = lines2.pop(0)
    if next_line == 'noop':
        render_cycle()
    else:
        render_cycle()
        render_cycle()
        register += int(next_line.split(' ')[1])

result = '\n'.join(render)
print(f'DAY 10 PART 2:\n{result}\n')
