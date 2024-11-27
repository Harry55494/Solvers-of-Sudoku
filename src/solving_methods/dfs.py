from solver import Solver
from src.board import Board
import os


class DFS(Solver):

    def __init__(self, starting_board: Board):
        super().__init__(starting_board)
        self.solved_board = None

    def solve_board(self):

        stack = [self.starting_board]
        while stack:
            current_board = stack.pop()

            if current_board.is_solved():
                self.solved_board = current_board
                break

            if not current_board.is_valid():
                continue

            os.system("clear")
            current_board.print_board()

            for y, row in enumerate(current_board.current_board):
                for x, item in enumerate(row):
                    if item == ".":
                        for i in range(1, len(current_board.current_board) + 1):
                            new_board = Board(
                                [row.copy() for row in current_board.current_board]
                            )
                            new_board.set_item(x, y, str(i))
                            stack.append(new_board)

        return self.solved_board


if __name__ == "__main__":
    board_to_solve = Board(
        [
            [".", ".", "3", "."],
            ["2", ".", "4", "."],
            [".", ".", ".", "."],
            ["4", ".", ".", "."],
        ]
    )
    solver = DFS(board_to_solve)
    solver.solve_board()
    os.system("clear")
    solver.solved_board.print_board()
