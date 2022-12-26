##########
# PART 1 #
##########
lines = []
with open('input/day13.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', ''))
lines = [line for line in lines if line]

def in_order(left, right):
    for i in range(len(left)):
        if i == len(right):
            return False

        lval = left[i]
        rval = right[i]
        if isinstance(lval, int) and isinstance(rval, int):
            if lval == rval:
                continue
            return lval < rval
        
        if isinstance(lval, int):
            result = in_order([lval], rval)
            if result is not None:
                return result
            continue
        
        if isinstance(rval, int):
            result = in_order(lval, [rval])
            if result is not None:
                return result
            continue
        
        result = in_order(lval, rval)
        if result is not None:
            return result
    
    if len(left) < len(right):
        return True

    return None

ordered_sum = 0
for i in range (0, len(lines), 2):
    pair_index = i // 2 + 1
    left = eval(lines[i])
    right = eval(lines[i + 1])
    if in_order(left, right) != False:
        ordered_sum += pair_index

print(f'DAY 13 PART 1:\n{ordered_sum}\n')

##########
# PART 2 #
##########
from functools import cmp_to_key

def comparator(left, right):
    result = in_order(left, right)
    if result == True:
        return -1
    elif result is None:
        return 0
    else:
        return 1

all_packets = [eval(l) for l in lines]
all_packets.extend([[[2]], [[6]]])

decoder_key = 1
sorted_packets = sorted(all_packets, key=cmp_to_key(comparator))
for i, p in enumerate(sorted_packets):
    if p == [[2]] or p == [[6]]:
        decoder_key *= i + 1

print(f'DAY 13 PART 2:\n{decoder_key}\n')
