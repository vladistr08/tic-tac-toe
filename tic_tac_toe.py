from terminaltables import SingleTable
from fabulous.color import bold, bg256, fg256
from fabulous.color import blue
# import numpy as np
# the tic-tac-toe class



# the tic-tac-toe class
class Tic_tac_toe:
    # useful game atributes
    player_curent = ""
    board = []
    message = ""

    # the construnctor of the class
    def __init__(self, player_curent="X"):
        self.player_curent = player_curent
        # fill the board with ' ' characther
        self.board = [' ' for i in range(9)]

    # the main function where the game starts
    def start_game(self):
        print("This is the Board, the position where you put X or O is from 0-8 from left to right and up to down!")
        self.print_board()
        self.game_loop()
        if self.get_winner() == 'TIE':
            print("It is a TIE!")
        else:
            print("The winner is " + self.get_winner() + " congratulations!")

    def __line_win(self, sign):
        for i in range(0, 9, 3):
            if self.board[i] == sign and self.board[i + 1] == sign and self.board[i + 2] == sign:
                return True
        return False

    def __col_win(self, sign):
        for i in range(3):
            if self.board[i] == sign and self.board[i + 3] == sign and self.board[i + 6] == sign:
                return True
        return False

    def __diag_win(self, sign):
        if self.board[0] == sign and self.board[4] == sign and self.board[8] == sign:
            return True
        if self.board[2] == sign and self.board[4] == sign and self.board[6] == sign:
            return True
        return False

    def get_winner(self):
        # return 'X' 'O' or 'Tie' if the game is at end
        # return empty string if the game is running
        if self.__line_win('X') == True:
            return 'X'
        if self.__line_win('O') == True:
            return 'O'
        if self.__col_win('X') == True:
            return 'X'
        if self.__col_win('O') == True:
            return 'O'
        if self.__diag_win('X') == True:
            return 'X'
        if self.__diag_win('O') == True:
            return 'O'
        boolean_board = list(map(lambda x: x == ' ', self.board))
        if not any(boolean_board):
            return 'TIE'
        return ""

    def game_not_finished(self):
        if self.get_winner() == "":
            return True
        else:
            return False

    def user_input(self):
        intrare = input(bold("On wich position (0-8) :"))
        if len(intrare) != 1:
            return self.user_input()
        if ord('0') <= ord(intrare) <= ord('8'):
            return int(intrare)
        else:
            return self.user_input()

    # the main function where the game runs
    def game_loop(self):
        while self.game_not_finished():
            x = self.user_input()
            self.move(x)
            self.print_game()

    # puts X or O on the board and change the next sign
    def move(self, location):
        if self.board[location] != ' ':
            self.message = "Invalid Move"
        else:
            self.board[location] = self.player_curent
            if self.player_curent == 'X':
                self.player_curent = 'O'
            else:
                self.player_curent = 'X'

    def print_board(self):
        display_data = [cell + "\n" + blue(index) for index,
                        cell in enumerate(self.board)]

        data = [display_data[0:3], display_data[3:6], display_data[6:]]
        table = SingleTable(data)
        table.inner_row_border = True
        print(table.table)
        print()

    def print_game(self):
        print(bg256("blue", "Current Player: " + self.player_curent))
        print(bg256("red", self.message))
        self.message = ""
        self.print_board()
