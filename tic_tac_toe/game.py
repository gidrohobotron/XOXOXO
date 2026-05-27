from typing import List, Optional, Tuple

Board = List[List[str]]


def new_board() -> Board:
    return [[" " for _ in range(3)] for _ in range(3)]


def make_move(board: Board, row: int, col: int, mark: str) -> bool:
    if board[row][col] == " ":
        board[row][col] = mark
        return True
    return False


def check_winner(board: Board) -> Optional[str]:
    lines = []
    for i in range(3):
        lines.append(board[i])  # row
        lines.append([board[0][i], board[1][i], board[2][i]])  # col
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])
    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0]
    return None


def is_full(board: Board) -> bool:
    return all(cell != " " for row in board for cell in row)


def available_moves(board: Board) -> List[Tuple[int, int]]:
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]


def format_board(board: Board) -> str:
    rows = []
    for r in range(3):
        rows.append(" | ".join(board[r]))
        if r < 2:
            rows.append("-" * 9)
    return "\n".join(rows)
