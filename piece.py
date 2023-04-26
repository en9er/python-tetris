import random


class Piece:
    # 4x4 max piece size
    size = 4
    shape = [[]]

    def __str__(self):
        res = f"rotations: {self.rotations}\n"
        for row in self.shape:
            res += f"{row}\n"
        return res

    def transpose(self):
        self.shape = list(zip(*self.shape[::-1]))

    def transpose_neg(self):
        self.shape = list(zip(*self.shape))[::-1]

    def rotate_random_times(self):
        # max rotations 3, the 4th is the same as initial one
        self.rotations = random.randint(0, 3)
        if self.rotations:
            if self.rotations > 2:
                self.transpose_neg()
            else:
                for _ in range(self.rotations):
                    self.transpose()

    _piece_shape = {
        "S": [['.', '.', '.', '.'],
              ['.', '*', '*', '.'],
              ['*', '*', '.', '.'],
              ['.', '.', '.', '.']],

        "I": [['.', '*', '.', '.'],
              ['.', '*', '.', '.'],
              ['.', '*', '.', '.'],
              ['.', '*', '.', '.']],

        "L": [['.', '*', '.', '.'],
              ['.', '*', '.', '.'],
              ['.', '*', '*', '.'],
              ['.', '.', '.', '.']],

        "T": [['.', '.', '.', '.'],
              ['.', '*', '.', '.'],
              ['*', '*', '*', '.'],
              ['.', '.', '.', '.']],

        "O": [['.', '.', '.', '.'],
              ['.', '*', '*', '.'],
              ['.', '*', '*', '.'],
              ['.', '.', '.', '.']],
    }

    def __init__(self):
        self.shape = [['.' for _ in range(self.size)] for _ in range(self.size)]
        # random piece type
        self.shape = self._piece_shape[random.choice(list(self._piece_shape.keys()))]
        # define rotation
        self.rotations = 0
        self.rotate_random_times()
        self.position_X = 0
        self.position_Y = 0
        self.piece_coords = []
        for i in range(Piece.size):
            for j in range(Piece.size):
                if self.shape[i][j] == '*':
                    self.piece_coords.append([i, j])

