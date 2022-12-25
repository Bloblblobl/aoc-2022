##########
# PART 1 #
##########
file_tree = {}
wd_path = []

def get_d(path=None):
    if path is None:
        path = wd_path

    current_dir = file_tree
    for part in path:
        current_dir = current_dir[part]
    return current_dir

with open('input/day7.txt', 'r') as f:
    for line in f.readlines():
        stripped_line = line.replace('\n', '').strip()
        if stripped_line.startswith('$ cd /'):
            wd_path = []
        elif stripped_line.startswith('$ cd ..'):
            wd_path.pop()
        elif stripped_line.startswith('$ cd '):
            new_dir = stripped_line.replace('$ cd ', '')
            current_dir = get_d()
            if new_dir not in current_dir:
                current_dir[new_dir] = {}
            wd_path.append(stripped_line.replace('$ cd ', ''))
        elif stripped_line.startswith('$ ls'):
            continue
        else:
            current_dir = get_d()
            prefix, name = stripped_line.split(' ')
            if prefix == 'dir':
                if name not in current_dir:
                    current_dir[name] = {}
            else:
                current_dir[name] = int(prefix)

dir_sizes = []

def traverse_count(current_dir=None, path=None):
    if current_dir is None:
        current_dir = file_tree
        path = []
    
    dir_size = 0
    for name, value in current_dir.items():
        if type(value) == dict:
            dir_size += traverse_count(value, path + [name])
        else:
            dir_size += value
    
    dir_sizes.append(dir_size)
    return dir_size

total_size = traverse_count()

total_below_limit = sum([size for size in dir_sizes if size <= 100000])

print(f'DAY 7 PART 1:\n{total_below_limit}\n')

##########
# PART 2 #
##########
total_disk_space = 70000000
unused_space_needed = 30000000
unused_space = total_disk_space - total_size
space_to_free = unused_space_needed - unused_space
min_dir_size = None

for size in dir_sizes:
    if size >= space_to_free and (min_dir_size is None or size < min_dir_size):
        min_dir_size = size

print(f'DAY 7 PART 2:\n{min_dir_size}\n')
