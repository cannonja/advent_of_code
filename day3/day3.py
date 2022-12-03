import string



letters = string.ascii_lowercase + string.ascii_uppercase
priorities = {l:i for l, i in zip(letters, range(1, len(letters) + 1))}

s = 'vJrwpWtwJgWrhcsFMMfFFhFp'
s1 = set(s[:(len(s)//2)])
s2 = set(s[(len(s)//2):])
common = s1.intersection(s2).pop()
priority = priorities[common]


def part_one(input_path):
    letters = string.ascii_lowercase + string.ascii_uppercase
    priorities = {l:i for l, i in zip(letters, range(1, len(letters) + 1))}
    tot_priority = 0
    with open(input_path, 'r') as fh:
        for line in fh:
            s = line.strip()
            s1 = set(s[:(len(s)//2)])
            s2 = set(s[(len(s)//2):])
            common = s1.intersection(s2).pop()
            tot_priority += priorities[common]
    print(f"Total priority = {tot_priority}")


def part_two(input_path):
    letters = string.ascii_lowercase + string.ascii_uppercase
    priorities = {l:i for l, i in zip(letters, range(1, len(letters) + 1))}
    tot_priority = 0
    tmp = []
    with open(input_path, 'r') as fh:
        for i, line in enumerate(fh):
            s = line.strip()
            tmp.append(set(s))
            if (i + 1) % 3 == 0:
                tset = tmp[0]
                for s in tmp[1:]:
                    tset = tset.intersection(s)
                tot_priority += priorities[tset.pop()]
                tmp = []
    print(f"Total priority = {tot_priority}")    








if __name__ == '__main__':
    input_path = 'input.txt'
    part_one(input_path)
    part_two(input_path)
