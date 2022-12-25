##########
# PART 1 #
##########
lines = []
with open('input/day8.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', ''))

top_vis_map = {}
right_vis_map = {}
bottom_vis_map = {}
left_vis_map = {}
w = len(lines[0])
h = len(lines)

highest_top = 0
highest_bottom = 0
for x in range(w):
    for y in range(h):
        top_p = (x, y)
        bottom_p = (x, h - y - 1)
        top_h = lines[y][x]
        bottom_h = lines[h - y - 1][x]
        if y == 0:
            top_vis_map[top_p] = True
            bottom_vis_map[bottom_p] = True
            highest_top = top_h
            highest_bottom = bottom_h
        else:
            if top_h > highest_top:
                top_vis_map[top_p] = True
                highest_top = top_h
            else:
                top_vis_map[top_p] = False
            if bottom_h > highest_bottom:
                bottom_vis_map[bottom_p] = True
                highest_bottom = bottom_h
            else:
                bottom_vis_map[bottom_p] = False

highest_left = 0
highest_right = 0
for y in range(h):
    for x in range(w):
        left_p = (x, y)
        right_p = (w - x - 1, y)
        left_h = lines[y][x]
        right_h = lines[y][w - x - 1]
        if x == 0:
            left_vis_map[left_p] = True
            right_vis_map[right_p] = True
            highest_left = left_h
            highest_right = right_h
        else:
            if left_h > highest_left:
                left_vis_map[left_p] = True
                highest_left = left_h
            else:
                left_vis_map[left_p] = False
            if right_h > highest_right:
                right_vis_map[right_p] = True
                highest_right = right_h
            else:
                right_vis_map[right_p] = False

visible_count = 0
for x in range(w):
    for y in range(h):
        p = (x, y)
        if (
            top_vis_map[p] or
            right_vis_map[p] or
            bottom_vis_map[p] or
            left_vis_map[p]
        ):
            visible_count += 1

print(f'DAY 8 PART 1:\n{visible_count}\n')

##########
# PART 2 #
##########
top_scenic_score = 0
for x in range(w):
    for y in range(h):
        v = lines[y][x]

        # scan top
        top_score = 0
        for yy in range(1, y + 1):
            tv = lines[y - yy][x]
            top_score += 1
            if tv >= v:
                break

        # scan right
        right_score = 0
        for xx in range(1, w - x):
            rv = lines[y][x + xx]
            right_score += 1
            if rv >= v:
                break

        # scan bottom
        bottom_score = 0
        for yy in range(1, h - y):
            bv = lines[y + yy][x]
            bottom_score += 1
            if bv >= v:
                break

        # scan left
        left_score = 0
        for xx in range(1, x + 1):
            lv = lines[y][x - xx]
            left_score += 1
            if lv >= v:
                break
        
        scenic_score = top_score * right_score * bottom_score * left_score
        if scenic_score > top_scenic_score:
            top_scenic_score = scenic_score

print(f'DAY 8 PART 2:\n{top_scenic_score}\n')
    