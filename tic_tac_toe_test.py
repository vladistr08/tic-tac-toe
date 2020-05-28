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
