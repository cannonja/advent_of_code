import re


def extract_crates(stacks, line):
    i = 0
    stack_idx = i // 4
    while i < len(line):
        c = line[i]
        if i % 4 == 0 and c == '[':
            stack_idx = i // 4
            stacks[stack_idx].insert(0, line[i + 1])
        i += 1


def extract_move(line):
    pattern = r'move (\d+) from (\d+) to (\d+)'
    m = re.search(pattern, line)
    if m is not None:
        a, b, c = map(int, m.groups())

        return a, b - 1, c - 1


def move_crates(stacks, n, src, dst):
    for _ in range(n):
        crate = stacks[src].pop()
        stacks[dst].append(crate)


def move_crates_9001(stacks, n, src, dst):
    tmp = []
    for _ in range(n):
        crate = stacks[src].pop()
        tmp.insert(0, crate)
    stacks[dst].extend(tmp)


def part_one(input_path):
    stacks = [list() for _ in range(9)]
    with open(input_path, 'r') as fh:
        # Extract crates
        for line in fh:
            if '1' in line:
                break
            extract_crates(stacks, line)

        # Move crates
        for line in fh:
            if 'move' in line:
                n, src, dst = extract_move(line)
                move_crates(stacks, n, src, dst)
    
    # Build message
    msg = ''
    for s in stacks:
        msg += s[-1]
    print(f"The crates on the top are '{msg}'")


def part_two(input_path):
    stacks = [list() for _ in range(9)]
    with open(input_path, 'r') as fh:
        # Extract crates
        for line in fh:
            if '1' in line:
                break
            extract_crates(stacks, line)

        # Move crates
        for line in fh:
            if 'move' in line:
                n, src, dst = extract_move(line)
                move_crates_9001(stacks, n, src, dst)
    
    # Build message
    msg = ''
    for s in stacks:
        msg += s[-1]
    print(f"The crates on the top are '{msg}'")





if __name__ == '__main__':
    input_path = 'input.txt'
    part_one(input_path)
    part_two(input_path)
