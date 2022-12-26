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
