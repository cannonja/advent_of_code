

def mkr_generator(line):
    for i in range(len(line)):
        end = i + 4
        ss = line[i: end]
        if len(set(ss)) == 4:
            yield end


def msg_generator(line):
    for i in range(len(line)):
        end = i + 14
        ss = line[i: end]
        if len(set(ss)) == 14:
            yield end




def part_one(input_path):
    with open(input_path) as fh:
        line = fh.read().strip()
    gen = mkr_generator(line)
    mkr = next(gen)
    print(f"The first marker is {mkr}")


def part_two(input_path):
    with open(input_path) as fh:
        line = fh.read().strip()
    gen = msg_generator(line)
    mkr = next(gen)
    print(f"The first message is {mkr}")


if __name__ == '__main__':
    input_path = 'input.txt'
    part_one(input_path)
    part_two(input_path)
