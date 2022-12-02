

if __name__ == '__main__':
    #input_path = 'test_input1.txt'
    input_path = 'input.txt'
    max_elf_id = None
    max_elf_cal = 0
    cur_cal = 0
    elf_id = 1
    with open(input_path, 'r') as fh:
        for line in fh:
            if line.strip() == '':
                if cur_cal > max_elf_cal:
                    max_elf_cal = cur_cal
                    max_elf_id = elf_id
                    cur_cal = 0
                elf_id += 1
            else:
                cals = int(line.strip())
                cur_cal += cals
    print(f"Max elf ID: {max_elf_id}\nMax elf cals: {max_elf_cal}")