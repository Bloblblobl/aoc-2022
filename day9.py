##########
# PART 1 #
##########
lines = []
with open('input/day9.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', ''))

hx = 0
hy = 0
tx = 0
ty = 0

visited = set([(0,0)])
for line in lines:
    d, n = line.split(' ')
    for _ in range(int(n)):
        if d == 'U':
            hy += 1
            dx, dy = hx - tx, hy - ty
            if dy > 1:
                ty += 1
                if bool(dx):
                    tx += dx

        elif d == 'R':
            hx += 1
            dx, dy = hx - tx, hy - ty
            if dx > 1:
                tx += 1
                if bool(dy):
                    ty += dy

        elif d == 'D':
            hy -= 1
            dx, dy = hx - tx, hy - ty
            if dy < -1:
                ty -= 1
                if bool(dx):
                    tx += dx

        elif d == 'L':
            hx -= 1
            dx, dy = hx - tx, hy - ty
            if dx < -1:
                tx -= 1
                if bool(dy):
                    ty += dy
        
        visited.add((tx, ty))

print(f'DAY 9 PART 1:\n{len(visited)}\n')

##########
# PART 2 #
##########
rope_length = 10
rope = [[0, 0] for _ in range(rope_length)]
visited = set([(0,0)])

def adjust_rope(r, last_r):
    dx, dy = last_r[0] - r[0], last_r[1] - r[1]
    if dx > 1:
        r[0] += 1
        if dy <= -1:
            r[1] -= 1
        elif dy >= 1:
            r[1] += 1

    elif dx < -1:
        r[0] -= 1
        if dy <= -1:
            r[1] -= 1
        elif dy >= 1:
            r[1] += 1

    elif dy > 1:
        r[1] += 1
        if dx <= -1:
            r[0] -= 1
        elif dx >= 1:
            r[0] += 1

    elif dy < -1:
        r[1] -= 1
        if dx <= -1:
            r[0] -= 1
        elif dx >= 1:
            r[0] += 1

for line in lines:
    d, n = line.split(' ')
    for _ in range(int(n)):
        h = rope[0]
        if d == 'U':
            h[1] += 1

        elif d == 'R':
            h[0] += 1

        elif d == 'D':
            h[1] -= 1

        elif d == 'L':
            h[0] -= 1
        
        for i in range(1, rope_length):
            adjust_rope(rope[i], rope[i - 1])
                
        t = rope[-1]
        
        visited.add((t[0], t[1]))
    
print(f'DAY 9 PART 2:\n{len(visited)}\n')
