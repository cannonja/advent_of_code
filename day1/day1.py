
def part_one(input_path):
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
        
        if cur_cal > max_elf_cal:
            max_elf_cal = cur_cal
            max_elf_id = elf_id
            cur_cal = 0
    print(f"Max elf ID: {max_elf_id}\nMax elf cals: {max_elf_cal}")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __gt__(self, other):
        if self.value > other.value:
            return True

        return False

    def __ge__(self, other):
        if self.value >= other.value:
            return True

        return False

    def __repr__(self):
        return f"[{self.value}]_[{self.next}]"


class TopKList:
    def __init__(self, head=None, max_nodes=3):
        self.head = head
        self.max_nodes = max_nodes
        self.nodes = 0

    def __len__(self):
        return self.nodes

    def __repr__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.value))
            current = current.next
        
        print(nodes)
        return ' -> '.join(nodes)

    def add(self, value):
        node = Node(value)

        # List is empty
        if self.head is None:
            self.head = node
            self.nodes += 1
            return self

        # Node is max
        if node > self.head:
            tmp = self.head
            self.head = node
            self.head.next = tmp
            self.nodes += 1
            if self.nodes > self.max_nodes:
                self._trim()
            return self

        # List has one node
        if self.nodes == 1:
            self.head.next = node
            self.nodes += 1
            return self

        previous = self.head
        current = self.head.next
        while current is not None:
            #print(current)
            if node >= current:
                node.next = current
                previous.next = node
                self.nodes += 1
                if self.nodes > self.max_nodes:
                    self._trim()
                return self
            previous = current
            current = current.next
            print(current is None)

        return self

    def _trim(self):
        current = self.head
        for _ in range(self.max_nodes):
            current = current.next
        current.next = None
        self.nodes -= 1

                
        

        





def part_two():
    pass




if __name__ == '__main__':
    #input_path = 'test_input1.txt'
    #input_path = 'test_input2.txt'
    input_path = 'input.txt'
    part_one(input_path)
    