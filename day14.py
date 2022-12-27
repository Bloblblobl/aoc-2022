##########
# PART 1 #
##########
lines = []
with open('input/day14.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', ''))

split_lines = [line.split(' -> ') for line in lines]
split_points = [[point.split(',') for point in line] for line in split_lines]
paths = [[(int(x), int(y)) for x, y in points] for points in split_points]

unadjusted_source = (500, 0)
min_x, min_y = unadjusted_source
max_x, max_y = unadjusted_source
for path in paths:
    for point in path:
        x, y = point
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

adjusted_paths = [[(x - min_x, y - min_y) for x, y in path] for path in paths]
source = (unadjusted_source[0] - min_x, unadjusted_source[1] - min_y)
max_x -= min_x
max_y -= min_y
min_x, min_y = 0, 0
grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
grid[source[1]][source[0]] = '+'

for path in adjusted_paths:
    for i in range(1, len(path)):
        x1, y1 = path[i - 1]
        x2, y2 = path[i]
        small_x, small_y = min(x1, x2), min(y1, y2)
        big_x, big_y = max(x1, x2), max(y1, y2)
        for x in range(small_x, big_x + 1):
            for y in range(small_y, big_y + 1):
                grid[y][x] = '#'

def print_grid(pos=None):
    px, py = -1, -1
    if pos is not None:
        px, py = pos

    result = ''
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if x == px and y == py:
                result += 'C'
            else:
                result += grid[y][x]
        result += '\n'
    print(result)

def is_blocked(pos):
    px, py = pos
    if px < min_x or px > max_x:
        return False

    gval = grid[py][px]
    return gval == '#' or gval == 'O'

def get_next_pos(pos):
    px, py = pos
    if py == max_y:
        return None

    down_pos = (px, py + 1)
    left_pos = (px - 1, py + 1)
    right_pos = (px + 1, py + 1)

    if not is_blocked(down_pos):
        return down_pos
    
    if not is_blocked(left_pos):
        return left_pos
    
    if not is_blocked(right_pos):
        return right_pos
    
    return None

def add_sand(pos):
    px, py = pos
    if px < min_x or px > max_x:
        return 0
    
    grid[py][px] = 'O'
    return 1

reached_abyss = False
result = 0
while not reached_abyss:
    pos = source
    while (next_pos := get_next_pos(pos)) is not None:
        pos = next_pos
        if pos[1] == max_y:
            reached_abyss = True

    if not reached_abyss:
        result += add_sand(pos)

print_grid()
print(f'DAY 14 PART 1:\n{result}\n') 
