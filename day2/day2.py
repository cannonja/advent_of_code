

class RPSGame:
    def __init__(self):
        self.moves = {
            'X': 1,
            'Y': 2,
            'Z': 3
        }


    def play(self, opponent, move):
        if opponent == 'A':
            if move == 'X':
                return 3
            elif move == 'Y':
                return 6
            else:
                return 0
        elif opponent == 'B':
            if move == 'X':
                return 0
            elif move == 'Y':
                return 3
            else:
                return 6
        else:
            if move == 'X':
                return 6
            elif move == 'Y':
                return 0
            else:
                return 3


    def reverse_play(self, opponent, move):
        if opponent == 'A':
            if move == 'X':
                return self.moves['Z']
            elif move == 'Y':
                return 3 + self.moves['X']
            else:
                return 6 + self.moves['Y']
        elif opponent == 'B':
            if move == 'X':
                return self.moves['X']
            elif move == 'Y':
                return 3 + self.moves['Y']
            else:
                return 6 + self.moves['Z']
        else:
            if move == 'X':
                return self.moves['Y']
            elif move == 'Y':
                return 3 + self.moves['Z']
            else:
                return 6 + self.moves['X']


    def evaluate(self, opponent, move):
        result = self.play(opponent, move)

        return self.moves[move] + result


def part_one(input_path):
    game = RPSGame()
    tot_score = 0
    with open(input_path, 'r') as fh:
        for line in fh:
            opponent, move = line.strip().split()
            score = game.evaluate(opponent, move)
            tot_score += score
    print(f"Total score = {tot_score}")


def part_two(input_path):
    game = RPSGame()
    tot_score = 0
    with open(input_path, 'r') as fh:
        for line in fh:
            opponent, move = line.strip().split()
            score = game.reverse_play(opponent, move)
            tot_score += score
    print(f"Total score = {tot_score}")





if __name__ == '__main__':
    input_path = 'input.txt'
    part_one(input_path)
    part_two(input_path)
