from dataclasses import dataclass


@dataclass
class DirSum:
    value: int = 0



class Node:
    def __init__(self, name, size=0, is_dir=False):
        self.name = name
        self._size = size
        self.is_dir = is_dir
        self.children = []

    
    def add_child(self, node):
        self.children.append(node)


    def calculate_size(self):
        if self.is_dir:
            for child in self.children:
                self._size += child.calculate_size()

        return self._size


    def sum_large_dirs(self, dir_sum):
        if self.is_dir:
            for child in self.children:
                self._size += child.sum_large_dirs(dir_sum)
            if self._size <= 100000:
                dir_sum.value += self._size


    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, value):
        self._size = value


    def __repr__(self):
        return f"name = {self.name}, size = {self._size}, nchildren = {len(self.children)}"


class ElfFS:
    def __init__(self, root):
        self.root = root


    







def part_one(input_path):
    pass


def part_two(input_path):
    pass


if __name__ == '__main__':
    input_path = 'input.txt'
    part_one(input_path)
    part_two(input_path)
