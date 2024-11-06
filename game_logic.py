
class FiveInARowMinMax:
    def __init__(self, board_size=8, step_depth=1):
        self.board_size = board_size
        self.step_depth = step_depth
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.opponent = 'O'

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self, row, col):
        def check_line(line):
            count = 0
            for cell in line:
                if cell == self.current_player:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
            return False

        # Check horizontal line
        if check_line(self.board[row]):
            return True

        # Check vertical line
        if check_line([self.board[i][col] for i in range(self.board_size)]):
            return True

        # Check main diagonal
        main_diag = [self.board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))]
        main_diag.extend(
            self.board[i][j] for i, j in zip(range(row + 1, self.board_size), range(col + 1, self.board_size)))
        if check_line(main_diag):
            return True

        # Check secondary diagonal
        sec_diag = [self.board[i][j] for i, j in zip(range(row, -1, -1), range(col, self.board_size))]
        sec_diag.extend(self.board[i][j] for i, j in zip(range(row + 1, self.board_size), range(col - 1, -1, -1)))
        if check_line(sec_diag):
            return True

        return False

    def is_board_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def switch_player(self):
        self.current_player, self.opponent = self.opponent, self.current_player

    def get_empty_cells(self):
        return [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] == ' ']

    def evaluate_board(self):
        score = 0

        for i in range(self.board_size):
            for j in range(self.board_size - 4):
                score += self.evaluate_window(self.board[i][j:j + 5])

        for j in range(self.board_size):
            for i in range(self.board_size - 4):
                score += self.evaluate_window([self.board[x][j] for x in range(i, i + 5)])

        for i in range(self.board_size - 4):
            for j in range(self.board_size - 4):
                score += self.evaluate_window([self.board[i + x][j + x] for x in range(5)])
                score += self.evaluate_window([self.board[i + x][j + 4 - x] for x in range(5)])

        return score

    def evaluate_window(self, window):
        x_count = window.count('X')
        o_count = window.count('O')

        if x_count == 5:
            return 100
        elif o_count == 5:
            return -100
        elif x_count == 4 and window.count(' ') == 1:
            return 10
        elif o_count == 4 and window.count(' ') == 1:
            return -10
        elif x_count == 3 and window.count(' ') == 2:
            return 5
        elif o_count == 3 and window.count(' ') == 2:
            return -5
        else:
            return 0

    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.is_board_full():
            return self.evaluate_board()

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_empty_cells():
                i, j = move
                if self.make_move(i, j):
                    eval = self.minimax(depth - 1, alpha, beta, False)
                    self.board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_empty_cells():
                i, j = move
                if self.make_move(i, j):
                    eval = self.minimax(depth - 1, alpha, beta, True)
                    self.board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    def find_best_move(self):
        best_move = None
        best_eval = float('-inf')

        for move in self.get_empty_cells():
            i, j = move
            self.board[i][j] = self.opponent
            eval = self.minimax(self.step_depth, float('-inf'), float('inf'), False)
            self.board[i][j] = ' '

            if eval > best_eval:
                best_eval = eval
                best_move = move

        return best_move


