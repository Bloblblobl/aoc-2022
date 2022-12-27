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
