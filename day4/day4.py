
def build_set(s):
    b, e = s.split('-')
    
    return set(range(int(b), int(e) + 1))


def part_one(input_path):
    with open(input_path) as fh:
        ncontained = 0
        for line in fh:
            _s1, _s2 = line.strip().split(',')
            s1 =  build_set(_s1)
            s2 =  build_set(_s2)
            union = s1.union(s2)
            if union == s1 or union == s2:
                ncontained += 1
    print(f"There are {ncontained} contained assignments")


def part_two(input_path):
    with open(input_path) as fh:
        noverlapped = 0
        for line in fh:
            _s1, _s2 = line.strip().split(',')
            s1 =  build_set(_s1)
            s2 =  build_set(_s2)
            intersection = s1.intersection(s2)
            if intersection:
                noverlapped += 1
    print(f"There are {noverlapped} overlapping assignments")





if __name__ == '__main__':
    input_path = 'input.txt'
    part_one(input_path)
    part_two(input_path)
