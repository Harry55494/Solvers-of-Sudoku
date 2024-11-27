import termcolor


class Board:

    def __init__(self, array):
        self.definite_board = array
        self.current_board = array

    def print_board(self):
        for y, row in enumerate(self.current_board):
            if y % 3 == 0 and y != 0:
                print(" -" * len(row))
            for x, item in enumerate(row):
                if self.definite_board[y][x] == ".":
                    termcolor.cprint(item, "red", end=" ")
                else:
                    termcolor.cprint(item, "green", end=" ")
                if x % 3 == 2:
                    print("|", end=" ")
            print()

    def set_item(self, x, y, value):
        self.current_board[y][x] = value

    def is_valid(self):
        return self.is_valid_rows() and self.is_valid_columns()

    def is_row_valid(self, row):
        row = [alpha for alpha in row if alpha != "."]
        row_1 = row.copy()
        row_1.sort()
        set_1 = list(set(row))
        set_1.sort()
        return row_1 == set_1

    def is_valid_rows(self):
        for row in self.current_board:
            if not self.is_row_valid(row):
                return False
        return True

    def is_valid_columns(self):
        for x in range(len(self.current_board[0])):
            column = [
                self.current_board[y][x]
                for y in range(len(self.current_board))
                if self.current_board[y][x] != "."
            ]
            column_1 = column.copy()
            column_1.sort()
            set_1 = list(set(column))
            set_1.sort()
            if column_1 != set_1:
                return False
        return True

    def no_missing_values(self):
        for row in self.current_board:
            for item in row:
                if item == ".":
                    return False
        return True

    def is_solved(self):
        return self.is_valid() and self.is_valid_columns() and self.no_missing_values()


if __name__ == "__main__":
    board = Board([[".", ".", "."], ["2", "3", "1"], ["3", "1", "2"]])
    board.print_board()
    print(board.is_valid())

    board = Board([["1", "2", "3"], ["2", "3", "1"], ["3", "1", "."]])
    board.print_board()
    print(board.is_valid())
