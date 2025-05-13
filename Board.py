class GenerateBoard:
    def __init__(self, size = 3):
        self.size = size
        self.player = 1
        self.player_move = "X"
        self.board = self.generate_board()

    def generate_board(self):
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(None)
            board.append(row)
        return board

    def print_board(self):
        for i, row in enumerate(self.board):
            # Convert None to empty space for display
            row_display = [cell if cell is not None else ' ' for cell in row]
            print(f" {' | '.join(row_display)} ")
            if i < self.size - 1:
                print("-" * (4 * self.size - 1))
