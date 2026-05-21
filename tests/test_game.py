from tic_tac_toe.game import new_board, make_move, check_winner, is_full

def test_make_move_and_winner_row():
    b = new_board()
    make_move(b, 0, 0, "X")
    make_move(b, 0, 1, "X")
    make_move(b, 0, 2, "X")
    assert check_winner(b) == "X"

def test_is_full_and_draw():
    b = [["X","O","X"],["X","O","O"],["O","X","X"]]
    assert is_full(b) is True
    assert check_winner(b) is None
