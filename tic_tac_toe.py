class Tic_tac_toe:
    player_curent = ""
    board = []
    message = ""

    def __init__(self, player_curent = "X"):
        self.player_curent = player_curent
        self.board = ['_' for i in range(9)]

    def start_game(self):
        self.print_board()
        self.game_loop()
        if self.get_winner() == 'TIE':
            print("It is a TIE!")
        else:
            print("The winner is " + self.get_winner() + " congratulations!") 

    def __line_win(self, sign):
        for i in range(0, 9, 3):
            if self.board[i] == sign and self.board[i+1] == sign and self.board[i+2] == sign:
                return True
        return False

    def __col_win(self, sign):
        for i in range(3):
            if self.board[i] == sign and self.board[i+3] == sign and self.board[i+6] == sign:
                return True
        return False

    def __diag_win(self, sign):
        if self.board[0] == sign and self.board[4] == sign and self.board[8] == sign:
            return True
        if self.board[2] == sign and self.board[4] == sign and self.board[6] == sign:
            return True
        return False

    def get_winner(self):
        # return 'X' 'O' sau 'Tie' daca e sfarsit de joc
        # return string gol daca nu e sfarsit de joc
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
        boolean_board = list(map(lambda x: x == '_', self.board))
        if not any(boolean_board):
            return 'TIE'
        return ""

    def game_not_finished(self):
        if self.get_winner() == "":
            return True
        else:
            return False
            
    def user_input(self):
        intrare =  input("Pe care casuta? (0-8) :")
        if len(intrare) != 1:
            return self.user_input()
        if ord(intrare) >= ord('0') and ord(intrare) <= ord('8'):
            return int(intrare)
        else:
            return self.user_input()

    def game_loop(self):
        while self.game_not_finished():
            x = self.user_input()
            self.move(x)
            self.print_game()

    def move(self, location):
        if self.board[location] != '_':
            self.message = "Invalid Move"
        else:
            self.board[location] = self.player_curent
            if self.player_curent == 'X':
                self.player_curent = 'O'
            else:
                self.player_curent = 'X' 

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i] + ' | ' + self.board[i+1] + ' | ' + self.board[i+2])
        print()

    def print_game(self):
        print("Current Player: " + self.player_curent)
        print(self.message)
        self.message = ""
        self.print_board()

