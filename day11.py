##########
# PART 1 #
##########
lines = []
with open('input/day11.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', '').strip())
lines = [line for line in lines if line]

lines1 = lines.copy()
monkeys = []
while len(lines1):
    lines1.pop(0)
    item_line = lines1.pop(0)
    op_line = lines1.pop(0)
    test_line = lines1.pop(0)
    test_true_line = lines1.pop(0)
    test_false_line = lines1.pop(0)

    items = [int(i) for i in item_line.split(': ')[1].split(', ')]
    op_text = op_line.split('= ')[1]
    divisible_by = int(test_line.split(' ')[-1])
    test_true = int(test_true_line.split(' ')[-1])
    test_false = int(test_false_line.split(' ')[-1])
    monkeys.append({
        'items': items,
        'op_text': op_text,
        'divisible_by': divisible_by,
        'test_true': test_true,
        'test_false': test_false,
    })

num_rounds = 20
inspection_map = {i: 0 for i in range(len(monkeys))}
for r in range(num_rounds):
    for i, m in enumerate(monkeys):
        items = m['items']
        while len(items):
            inspection_map[i] += 1
            item = items.pop(0)
            op = lambda old: eval(m['op_text'])
            new_item = op(item) // 3
            passes_test = new_item % m['divisible_by'] == 0
            next_monkey = m['test_true'] if passes_test else m['test_false']
            monkeys[next_monkey]['items'].append(new_item)

max1, max2 = sorted(inspection_map.values())[-2:]
result = max1 * max2
print(f'DAY 11 PART 1:\n{result}\n')
