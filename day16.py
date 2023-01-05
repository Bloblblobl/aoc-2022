##########
# PART 1 #
##########
lines = []
with open('input/day16.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', ''))

flow_rates = {}
connections = {}
for line in lines:
    valve_name, remainder = line.replace('Valve ', '').split(' has flow rate=')
    normalized_remainder = remainder.replace('tunnels', 'tunnel').replace('leads', 'lead').replace('valves', 'valve')
    flow_rate, connected = normalized_remainder.split('; tunnel lead to valve ')
    flow_rates[valve_name] = int(flow_rate)
    connections[valve_name] = connected.split(', ')

route_cache = {}

def find_max_pressure(current_valve='AA', remaining_time=30, opened_valves=None):
    if remaining_time <= 1:
        return 0

    if opened_valves is None:
        opened_valves = []
    
    current_key = (current_valve, remaining_time, ''.join(opened_valves))
    
    if current_key in route_cache:
        return route_cache[current_key]
    
    options = []
    for connection in connections[current_valve]:
        options.append(find_max_pressure(
            current_valve=connection,
            remaining_time=remaining_time - 1,
            opened_valves=opened_valves,
        ))
    
    flow_rate = flow_rates[current_valve]
    if flow_rate > 0 and current_valve not in opened_valves:
        possible_pressure = flow_rate * (remaining_time - 1)
        options.append(possible_pressure + find_max_pressure(
            current_valve=current_valve,
            remaining_time=remaining_time - 1,
            opened_valves=opened_valves + [current_valve],
        ))
    
    max_pressure = max(options)
    route_cache[current_key] = max_pressure
    return max_pressure

result = find_max_pressure()
print(f'DAY 16 PART 1:\n{result}\n')