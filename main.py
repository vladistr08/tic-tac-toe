# Clasa tic-tac-toe

class Tic_tac_toe:
    player_curent = ""
    board = []
    message = ""

    def __init__(self, player_curent = "X"):
        self.player_curent = player_curent
        self.board = ['_' for i in range(9)]

    # Preia miscarea unui jucator si transforma board-ul

    def game_not_finished(self):
        boolean_board = list(map(lambda x: x == '_', self.board))
        return any(boolean_board)

    def user_input(self):
        return int(input("Pe care casuta? :"))

    def game_loop(self):
        while self.game_not_finished():
            self.move(self.user_input())
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

game = Tic_tac_toe()
game.game_loop()