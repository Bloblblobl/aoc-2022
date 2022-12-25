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

