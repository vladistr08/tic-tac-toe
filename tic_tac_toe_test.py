from tic_tac_toe import Tic_tac_toe


def test_empty_game():
    game = Tic_tac_toe()
    assert game.board == ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    assert game.player_curent == "X"


def test_moves():
    game = Tic_tac_toe()
    game.move(0)
    assert game.board == ["X", "_", "_", "_", "_", "_", "_", "_", "_"]
    game.move(1)
    assert game.board == ["X", "O", "_", "_", "_", "_", "_", "_", "_"]
    game.move(2)
    assert game.board == ["X", "O", "X", "_", "_", "_", "_", "_", "_"]
    game.move(3)
    assert game.board == ["X", "O", "X", "O", "_", "_", "_", "_", "_"]
    game.move(4)
    assert game.board == ["X", "O", "X", "O", "X", "_", "_", "_", "_"]
    game.move(5)
    assert game.board == ["X", "O", "X", "O", "X", "O", "_", "_", "_"]
    game.move(6)
    assert game.board == ["X", "O", "X", "O", "X", "O", "X", "_", "_"]
    game.move(7)
    assert game.board == ["X", "O", "X", "O", "X", "O", "X", "O", "_"]
    game.move(8)
    assert game.board == ["X", "O", "X", "O", "X", "O", "X", "O", "X"]


def test_x_winner():
    game = Tic_tac_toe()
    for m in [0, 1, 4, 2, 8]:
        game.move(m)
    assert game.get_winner() == 'X'
    game = Tic_tac_toe()
    for m in range(7):
        game.move(m)
    assert game.get_winner() == 'X'


def test_o_winner():
    game = Tic_tac_toe()
    for m in [0, 4, 1, 3, 8, 5]:
        game.move(m)
    assert game.get_winner() == 'O'


def test_tie():
    game = Tic_tac_toe()
    for m in [0, 2, 1, 3, 5, 4, 6, 7, 8]:
        game.move(m)
    assert game.get_winner() == 'TIE'
