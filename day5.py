##########
# PART 1 #
##########
stacks = None

with open('input/day5.txt', 'r') as f:
    reached_instructions = False
    for line in f.readlines():
        line = line.replace('\n', '')
        if line == '':
            stacks = [list(reversed(stack)) for stack in stacks]
            reached_instructions = True
            continue

        if not reached_instructions:
            if stacks is None:
                stacks = [[] for _ in range((len(line) + 1) // 4)]
            for col in range(len(stacks)):
                chunk = line[4 * col:4 * col + 4].strip()
                if len(chunk) != 3:
                    continue

                stacks[col].append(chunk[1])

        else:
            _, move_count, _, from_col, _, to_col = line.split(' ')
            move_count = int(move_count)
            from_col = int(from_col) - 1
            to_col = int(to_col) - 1
            from_stack = stacks[from_col]
            to_stack = stacks[to_col]
            moved_crates = from_stack[-move_count:]
            stacks[from_col] = from_stack[:-move_count]
            to_stack.extend(reversed(moved_crates))

top_crates = ''.join([stack[-1] for stack in stacks])

print(f'DAY 5 PART 1:\n{top_crates}\n')

##########
# PART 2 #
##########
stacks = None

with open('input/day5.txt', 'r') as f:
    reached_instructions = False
    for line in f.readlines():
        line = line.replace('\n', '')
        if line == '':
            stacks = [list(reversed(stack)) for stack in stacks]
            reached_instructions = True
            continue

        if not reached_instructions:
            if stacks is None:
                stacks = [[] for _ in range((len(line) + 1) // 4)]
            for col in range(len(stacks)):
                chunk = line[4 * col:4 * col + 4].strip()
                if len(chunk) != 3:
                    continue

                stacks[col].append(chunk[1])

        else:
            _, move_count, _, from_col, _, to_col = line.split(' ')
            move_count = int(move_count)
            from_col = int(from_col) - 1
            to_col = int(to_col) - 1
            from_stack = stacks[from_col]
            to_stack = stacks[to_col]
            moved_crates = from_stack[-move_count:]
            stacks[from_col] = from_stack[:-move_count]
            to_stack.extend(moved_crates)

top_crates = ''.join([stack[-1] for stack in stacks])

print(f'DAY 5 PART 2:\n{top_crates}\n')