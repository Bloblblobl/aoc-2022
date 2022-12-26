##########
# PART 1 #
##########
grid = []
with open('input/day12.txt', 'r') as f:
    for line in f.readlines():
        grid.append(line.replace('\n', ''))
max_x = len(grid[0]) - 1
max_y = len(grid) - 1
start_pos = None
end_pos = None
for y, line in enumerate(grid):
    for x, square in enumerate(line):
        if square == 'S':
            start_pos = (x, y)
        if square == 'E':
            end_pos = (x, y)

def elevation(pos):
    x, y = pos
    e = grid[y][x]
    if e == 'S':
        e = 'a'
    if e == 'E':
        e = 'z'
    return ord(e)

def can_step(first_pos, second_pos):
    x2, y2 = second_pos
    if x2 < 0 or x2 > max_x:
        return False
    if y2 < 0 or y2 > max_y:
        return False
    return elevation(second_pos) - elevation(first_pos) <= 1

visited = {}
q = [(0, start_pos)]
while(len(q)):
    steps, pos = q.pop(0)
    x, y = pos
    next_steps = steps + 1
    e = elevation(pos)

    right = (x + 1, y)
    left = (x - 1, y)
    down = (x, y + 1)
    up = (x, y - 1)

    for direction in [right, left, down, up]:
        if not can_step(pos, direction):
            continue

        if direction not in visited or next_steps < visited[direction]:
            q.append((next_steps, direction))
            visited[direction] = next_steps

print(f'DAY 12 PART 1:\n{visited[end_pos]}\n')
