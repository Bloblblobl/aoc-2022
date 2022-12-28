##########
# PART 1 #
##########
lines = []
with open('input/day15.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', ''))

target_y = 2000000
sensors = set()
beacons = set()
empty_spaces = set()
sensor_ranges = []
for line in lines:
    sensor_string, beacon_string = line.split(': ')
    _, sensor_pos_string = sensor_string.split('x=')
    _, beacon_pos_string = beacon_string.split('x=')
    sensor_x, sensor_y = [int(i) for i in sensor_pos_string.split(', y=')]
    beacon_x, beacon_y = [int(i) for i in beacon_pos_string.split(', y=')]

    sensor_pos = (sensor_x, sensor_y) 
    beacon_pos = (beacon_x, beacon_y) 
    if sensor_pos in empty_spaces:
        empty_spaces.remove(sensor_pos)
    if beacon_pos in empty_spaces:
        empty_spaces.remove(beacon_pos)
    sensors.add(sensor_pos)
    beacons.add(beacon_pos)


    sensor_range = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    target_distance = abs(sensor_y - target_y)
    sensor_ranges.append((sensor_pos, sensor_range))
    if target_distance > sensor_range:
        continue

    for dx in range(0, sensor_range - target_distance + 1):
        positions = [
            (sensor_x + dx, target_y),
            (sensor_x - dx, target_y),
        ]
        for pos in positions:
            if pos not in beacons and pos not in sensors:
                empty_spaces.add(pos)

result = len(empty_spaces)
print(f'DAY 15 PART 1:\n{result}\n')

##########
# PART 2 #
##########
min_p = 0
max_p = 4000000

target_beacon = None
for i, (pos, r) in enumerate(sensor_ranges):
    sx, sy = pos
    bordering_points = set()
    for dy in range(r + 2):
        dx = r - dy + 1
        points = [
            (sx + dx, sy + dy),
            (sx + dx, sy - dy),
            (sx - dx, sy + dy),
            (sx - dx, sy - dy),
        ]
        for p in points:
            px, py = p
            if px < min_p or px > max_p or py < min_p or py > max_p:
                continue
            bordering_points.add(p)

    for border_point in bordering_points:
        bx, by = border_point
        out_of_reach = True
        for other_pos, other_range in sensor_ranges:
            if pos == other_pos or not out_of_reach:
                continue
            ox, oy = other_pos
            distance = abs(ox - bx) + abs(oy - by)
            if distance <= other_range:
                out_of_reach = False
        
        if out_of_reach:
            target_beacon = border_point
            break
    
    if target_beacon is not None:
        break

tx, ty = target_beacon
result = tx * max_p + ty
print(f'DAY 15 PART 2:\n{result}\n')
